---
name: tutorial-author
description: Use when creating or substantially editing CodeCamp lesson/tutorial content (Beginner or Advanced) in this repo — a new game tutorial, a new lesson set, a rewrite of an existing lesson. Drafts the content against CLAUDE.md, then runs an independent review pass before presenting it, so rule violations are caught before the user has to point them out.
---

# Tutorial Author

This skill exists because content review after the fact is unreliable — the same context that wrote the content tends to rationalize its own choices instead of spotting problems in them. Treat drafting and review as two separate passes with different vantage points, not one pass that both writes and grades itself.

## Step 1: Re-read CLAUDE.md fresh

Read `/CLAUDE.md` in full immediately before drafting, even if you read it earlier in the conversation. It is a living document in this repo and has changed mid-session before (the Advanced/Style rules in particular). Do not rely on a remembered summary of it.

Identify which section applies (Beginner or Advanced) and check the target directory for existing conventions to match: file naming, concept/task split, WIP vs Approved placement, README structure of sibling tutorials.

## Step 2: Draft

Write the content. Follow CLAUDE.md's Context, Style, and Other Restrictions sections exactly, plus whatever structural conventions Step 1 surfaced (e.g. Advanced tutorials currently split each lesson into a pure-theory `Lesson-0X-Title.md` and a hands-on `Lesson-0X-Title-Task.md`, per Beginner's concept/task file pattern).

New tutorials go in the relevant `WIP/` folder, not straight to `Approved/`, unless told otherwise.

## Step 3: Mechanical gates

Run these as plain shell commands over every new/changed file. These are deterministic — don't substitute a judgment call for a command that can just be run.

```bash
# No em-dashes anywhere (CLAUDE.md: "DO NOT use em-dashes")
grep -rn "—" <changed-files>

# No teacher-facing assessment language in Advanced content
# (CLAUDE.md: Advanced tutorials are self-guided and ungraded)
grep -rniE "teacher notes|assessment checklist|grading|rubric|instructor" <changed-files-under-Advanced>

# Every markdown cross-link resolves relative to its own file
# (walk each [text](path.md) link, resolve relative to dirname of the file, confirm it exists)

# For PyGame/code tutorials: every fenced code block that represents
# the cumulative "complete code" for a lesson should py_compile cleanly,
# and ideally run headlessly for a fixed number of frames:
#   SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy python3 <assembled_lesson.py>
```

Fix anything these catch before moving on. Do not ask a subagent to "check for em-dashes" — grep is faster and never misses one.

## Step 4: Independent review

Spawn a fresh subagent (Agent tool, general-purpose is fine) with:
- The full current text of `/CLAUDE.md`
- The full text of every new/changed file
- Explicitly **not** your drafting rationale or this conversation's history

Ask it to check the content against each CLAUDE.md rule one by one and report violations, plus flag any claim in the content that reads as more certain than what was actually verified (e.g. "this is compatible with CodeHS" when no CodeHS-specific testing happened — say what was actually checked instead of asserting compatibility).

A fresh subagent is the point here, not a formality: it has no investment in the choices already made, so it catches things the drafting pass rationalized past.

## Step 5: Fix or ask

- Clear rule violations (style, structure, restrictions): fix directly, then re-run Step 3's mechanical gates.
- Genuine judgment calls where CLAUDE.md is ambiguous or silent (e.g. how granular to split lessons, which of several valid structures to use): surface via AskUserQuestion rather than guessing and hoping it matches what the user wanted. Getting this wrong silently is exactly the failure mode this skill exists to avoid.

## Step 6: Report

When presenting the finished content, separate what was mechanically verified from what remains an assumption. For example: "0 em-dashes, all internal links resolve, code smoke-tested headlessly" is verified; "should be compatible with CodeHS's Pygame sandbox" is an inference from public docs, not a confirmed test — say so explicitly rather than letting a confident tone imply more certainty than exists.
