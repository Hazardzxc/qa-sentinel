---
description: Copy the qa-sentinel standards, templates and docs scaffold into the current QA repository
---
Set up the qa-sentinel scaffold in the current directory, which must be the independent QA automation Git repository (not the frontend or backend repo).

1. Run `git rev-parse --show-toplevel` and show the result. If this is not a Git repo, or looks like a frontend/backend source repo, stop and ask.
2. Shallow-clone `https://github.com/Hazardzxc/qa-sentinel` into a new temp directory.
3. Copy `<temp>/qa-automation/.` into the repo root with `cp -Rn` so no existing file is overwritten. List any files that were skipped because they already existed.
4. If `.claude/skills` does not exist, create it as a symlink to `../.agents/skills`.
5. Remove the temp directory, run `python3 scripts/validate_skill_set.py`, and report the result. Do not commit.
