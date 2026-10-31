# Workspace Rules: Fleet Harness (Claude Code)

## Strict Repository Boundary: No Applications Inside /fleet

1. **Fleet is strictly a harness**: This repository (`fleet`) only contains reusable agent skills (`skills/`) and the knowledge base (`wiki/`). **NEVER create or build application code inside this repository.**
2. **New Projects in Separate Repositories**: Whenever asked to build, scaffold, or develop an application or project (e.g., *"Please create TypeScript app for Photography company..."*):
   - Always create the new project in its own dedicated directory **outside** of `/fleet` (e.g., in `../<project-name>` or the user-specified project location).
   - Initialize a separate Git repository in that new project directory (`git init`).
   - If desired, link the skills from `fleet/skills` into the new project's `.agents/skills` or `.claude/skills`.
3. **Record Ventures in Fleet**: After completing work on an external project, use the `kb` skill to log the venture, decisions, and outcomes into `fleet/wiki/ventures/`.
