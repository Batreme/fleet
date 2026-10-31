---
name: kb
description: Consult or update the knowledge base (wiki) of past ventures, outcomes, and playbooks. Use when looking up context before starting a task, or when recording the outcome and lessons of completed work.
---

# Knowledge Base (KB / Wiki) Skill

The `wiki/` directory is an Obsidian-compatible knowledge base that stores historical venture records, outcomes, and reusable engineering playbooks.

Use this skill in two phases:
1. **At the start of a task**: to retrieve past context, check desired outcomes, and avoid repeating previous mistakes.
2. **At the end of a task**: to record what was done, what obstacles occurred, and what the final outcome was.

---

## 1. Consulting the KB (Before Starting Work)

When beginning a non-trivial task, feature, or refactor:

1. **Check the Index**: Read `wiki/INDEX.md` to identify relevant sections.
2. **Search Past Ventures**: Search `wiki/ventures/` for similar past attempts or projects:
   - What was the intended outcome?
   - What libraries, patterns, or architecture were chosen?
   - What obstacles or failures occurred?
3. **Review Playbooks**: Read relevant playbooks in `wiki/playbooks/` to adhere to established guidelines and avoid known anti-patterns.
4. **Apply Findings**: Factor previous lessons directly into your implementation plan.

---

## 2. Recording a Venture (After Completing Work)

When a task, PR, or major milestone is completed (or abandoned):

1. **Create a Venture Note**:
   - Location: `wiki/ventures/YYYY-MM-DD-<short-title>.md`
   - Use the template in `wiki/templates/venture-template.md`.
   - Ensure the YAML frontmatter includes:
     ```yaml
     ---
     title: "Venture: <Title>"
     date: YYYY-MM-DD
     status: completed # in-progress | completed | abandoned
     tags:
       - venture
       - <domain-tag>
     outcome_summary: "Concise summary of the final outcome."
     ---
     ```
2. **Document the Key Sections**:
   - **Context & Desired Outcome**: What was the goal?
   - **Approach Taken**: Key technical decisions.
   - **Challenges & Obstacles**: What went wrong or caused friction?
   - **Final Outcome**: The deliverable state (links to commits/PRs) and whether the goal was met.
   - **Reusable Lessons**: Actionable advice for future agents.
3. **Extract Playbooks (if applicable)**:
   - If the venture established a reusable pattern or standard, create or update a note in `wiki/playbooks/<topic>.md` using `wiki/templates/playbook-template.md`.
4. **Update the Index**:
   - Add a wikilink `[[YYYY-MM-DD-<short-title>]]` under the appropriate category in `wiki/INDEX.md`.

---

## 3. Formatting Standards

- **Obsidian Compatible**: Always use standard Markdown and wikilinks (`[[topic-name]]`) for referencing other notes.
- **Concise & Direct**: Focus on facts, decisions, and takeaways rather than verbose logs.
- **No Heavy Dependencies**: Keep all notes as plaintext Markdown with frontmatter; do not introduce external database dependencies.
