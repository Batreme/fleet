#!/usr/bin/env python3
"""
Fleet Agent Harness Runner
Lightweight manager to list, inspect, execute, and link agent personas across projects.
Designed for Antigravity (AGY) now, extensible to Claude.
Zero external dependencies (uses standard Python library).
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Paths relative to repository root
REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO_ROOT / "agents"
GLOBAL_AGENTS_DIR = AGENTS_DIR / "global"
PROJECT_AGENTS_DIR = AGENTS_DIR / "project"
MODELS_DIR = AGENTS_DIR / "models"


def parse_frontmatter(file_path: Path):
    """Parses frontmatter and body from a markdown file without external dependencies."""
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content.strip()

    raw_yaml, body = match.group(1), match.group(2).strip()
    metadata = {}
    current_key = None
    current_list = None

    for line in raw_yaml.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith("#"):
            continue

        # Handle list item
        if line_str.startswith("- ") and current_list is not None:
            val = line_str[2:].strip().strip("\"'")
            current_list.append(val)
            continue

        # Handle key: value
        if ":" in line_str:
            key, val = line_str.split(":", 1)
            key = key.strip()
            val = val.strip().strip("\"'")
            if not val:
                # Potential start of a list or empty mapping
                current_list = []
                metadata[key] = current_list
                current_key = key
            else:
                current_list = None
                current_key = key
                metadata[key] = val

    return metadata, body


def get_all_agents():
    """Returns a dict of all discovered agents keyed by name."""
    agents = {}
    search_dirs = [
        ("global", GLOBAL_AGENTS_DIR),
        ("project", PROJECT_AGENTS_DIR),
    ]

    for default_type, dir_path in search_dirs:
        if not dir_path.is_dir():
            continue
        for agent_file in dir_path.glob("*.md"):
            meta, body = parse_frontmatter(agent_file)
            name = meta.get("name", agent_file.stem)
            agents[name] = {
                "name": name,
                "role": meta.get("role", "Specialist"),
                "type": meta.get("type", default_type),
                "description": meta.get("description", "No description provided."),
                "tools": meta.get("tools", []),
                "file_path": agent_file,
                "system_prompt": body,
            }
    return agents


def get_model_config(model_backend: str):
    """Loads configuration for the specified model backend (agy or claude)."""
    cfg_file = MODELS_DIR / f"{model_backend.lower()}.json"
    if not cfg_file.is_file():
        raise FileNotFoundError(f"Model backend configuration not found: {cfg_file}")
    with open(cfg_file, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_list(args):
    """Lists all available agents in the fleet."""
    agents = get_all_agents()
    if not agents:
        print("No agents defined in the fleet.")
        return 0

    globals_list = [a for a in agents.values() if a["type"] == "global"]
    projects_list = [a for a in agents.values() if a["type"] == "project"]

    print("\n=== Fleet Agent Roster ===\n")
    if globals_list:
        print("[Global Agents] (Cross-project & architectural)")
        for a in globals_list:
            tools_str = f" (tools: {', '.join(a['tools'])})" if a['tools'] else ""
            print(f"  • {a['name']:<14} [{a['role']}]{tools_str}")
            print(f"    └─ {a['description']}")
        print()

    if projects_list:
        print("[Project Agents] (Domain & task execution)")
        for a in projects_list:
            tools_str = f" (tools: {', '.join(a['tools'])})" if a['tools'] else ""
            print(f"  • {a['name']:<14} [{a['role']}]{tools_str}")
            print(f"    └─ {a['description']}")
        print()

    print(f"Total: {len(agents)} agents available.\n")
    return 0


def cmd_show(args):
    """Shows detailed persona and settings for a given agent."""
    agents = get_all_agents()
    agent = agents.get(args.agent)
    if not agent:
        print(f"Error: Agent '{args.agent}' not found.", file=sys.stderr)
        return 1

    print(f"\nAgent:       {agent['name']}")
    print(f"Role:        {agent['role']}")
    print(f"Type:        {agent['type']}")
    print(f"Source:      {agent['file_path']}")
    print(f"Description: {agent['description']}")
    print(f"Tools:       {', '.join(agent['tools']) if agent['tools'] else 'None'}\n")
    print("--- System Prompt ---")
    print(agent["system_prompt"])
    print("---------------------\n")
    return 0


def cmd_run(args):
    """Executes an agent against a target project directory."""
    agents = get_all_agents()
    agent = agents.get(args.agent)
    if not agent:
        print(f"Error: Agent '{args.agent}' not found.", file=sys.stderr)
        return 1

    target_dir = Path(args.target).resolve() if args.target else Path.cwd()
    if not target_dir.is_dir():
        print(f"Error: Target path '{target_dir}' does not exist or is not a directory.", file=sys.stderr)
        return 1

    model_backend = args.backend.lower()
    try:
        model_cfg = get_model_config(model_backend)
    except FileNotFoundError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    cli_bin = model_cfg.get("cli_binary", model_backend)
    model_name = args.model or model_cfg.get("default_model")
    effort = args.effort or model_cfg.get("default_effort")

    print(f"Invoking [{agent['name']}] via backend [{model_backend}]")
    print(f"Target directory: {target_dir}")
    print(f"Model: {model_name} (effort: {effort})")

    if model_backend == "agy":
        cmd = [cli_bin]
        if args.model:
            cmd.extend(["--model", model_name])
        if effort:
            cmd.extend(["--effort", effort])
        if target_dir != Path.cwd():
            cmd.extend(["--add-dir", str(target_dir)])

        # Prompt mode or interactive mode
        if args.prompt:
            cmd.extend(["-i", f"Acting as {agent['name']} ({agent['role']}):\n{args.prompt}"])
        else:
            cmd.extend(["-i", f"You are acting as {agent['name']} ({agent['role']}). Wait for instructions."])

    elif model_backend == "claude":
        cmd = [cli_bin]
        if args.model:
            cmd.extend(["--model", model_name])
        if args.prompt:
            cmd.extend(["-p", f"Role: {agent['name']} ({agent['role']}). Task: {args.prompt}"])

    else:
        print(f"Error: Unsupported backend '{model_backend}'", file=sys.stderr)
        return 1

    print("\nCommand to execute:")
    print("  " + " ".join(cmd) + "\n")

    if args.dry_run:
        print("(Dry-run completed. Command not executed.)")
        return 0

    return subprocess.call(cmd, cwd=str(target_dir))


def cmd_link(args):
    """Links or registers the fleet into a target project workspace so AGY discovers it."""
    target_dir = Path(args.target).resolve()
    if not target_dir.is_dir():
        print(f"Error: Target path '{target_dir}' is not a directory.", file=sys.stderr)
        return 1

    target_agents_dir = target_dir / ".agents"
    target_rules_dir = target_agents_dir / "rules"
    target_rules_dir.mkdir(parents=True, exist_ok=True)

    # Generate an AGENTS.md rule summary in the target project
    agents = get_all_agents()
    agents_summary_file = target_rules_dir / "FLEET_AGENTS.md"

    lines = [
        "---",
        "name: fleet-agents",
        "description: Fleet agent roster and guidelines for this workspace.",
        "trigger: always_on",
        "---",
        "",
        "# Fleet Agent Roster for Workspace",
        "",
        "The following specialized agent personas are defined in the central fleet harness:",
        "",
    ]

    for a in agents.values():
        lines.append(f"### {a['name']} ({a['role']}) - [{a['type']}]")
        lines.append(f"{a['description']}")
        lines.append("")

    agents_summary_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Linked fleet definitions into: {agents_summary_file}")
    return 0


def cmd_export_claude(args):
    """Exports agent definitions into a CLAUDE.md file for Claude Code."""
    target_dir = Path(args.target).resolve() if args.target else Path.cwd()
    if not target_dir.is_dir():
        print(f"Error: Target path '{target_dir}' is not a directory.", file=sys.stderr)
        return 1

    agents = get_all_agents()
    claude_file = target_dir / "CLAUDE.md"

    lines = [
        "# Agent Fleet Directives (Claude)",
        "",
        "This project integrates with the central agent fleet harness.",
        "",
        "## Agent Roles & Personas",
        "",
    ]

    for a in agents.values():
        lines.append(f"### Role: {a['name'].upper()} ({a['role']})")
        lines.append(f"Scope: `{a['type']}`")
        lines.append(f"Summary: {a['description']}")
        lines.append("")
        lines.append("```markdown")
        lines.append(a["system_prompt"])
        lines.append("```")
        lines.append("")

    claude_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Exported Claude directives to: {claude_file}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Fleet: Autonomous Agent Fleet Harness for Antigravity & Claude",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    subparsers.add_parser("list", help="List all available agents in the fleet")

    # show
    show_p = subparsers.add_parser("show", help="Show details and persona of an agent")
    show_p.add_argument("agent", help="Agent identifier (e.g. architect, builder, tester, reviewer)")

    # run
    run_p = subparsers.add_parser("run", help="Run an agent against a target workspace")
    run_p.add_argument("agent", help="Agent identifier to run")
    run_p.add_argument("--backend", default="agy", choices=["agy", "claude"], help="Model backend (default: agy)")
    run_p.add_argument("--target", default=".", help="Target workspace path (default: current directory)")
    run_p.add_argument("--model", default=None, help="Override default model")
    run_p.add_argument("--effort", default=None, help="Reasoning effort level")
    run_p.add_argument("--prompt", default=None, help="Initial task or prompt to pass")
    run_p.add_argument("--dry-run", action="store_true", help="Print command without executing")

    # link
    link_p = subparsers.add_parser("link", help="Link fleet agent definitions to a target project (.agents)")
    link_p.add_argument("target", help="Path to target project directory")

    # export-claude
    exp_p = subparsers.add_parser("export-claude", help="Export agent roster to CLAUDE.md in target project")
    exp_p.add_argument("--target", default=".", help="Path to target project directory")

    args = parser.parse_args()

    commands = {
        "list": cmd_list,
        "show": cmd_show,
        "run": cmd_run,
        "link": cmd_link,
        "export-claude": cmd_export_claude,
    }

    cmd_fn = commands.get(args.command)
    if cmd_fn:
        return cmd_fn(args)
    return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
