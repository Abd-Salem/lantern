# Contributing to lantern

Thanks for helping out! These are the conventions our team follows.

## Branches
- Never commit directly to `main`; it is protected.
- Create a short-lived branch from an up-to-date `main` for every change.
- Name branches by type: `feature/<name>`, `fix/<name>`, `docs/<name>`.
- Delete the branch after its pull request is merged.

## Commit messages
- Format: `type(scope): short summary`, for example `feat(cli): add list --sort`.
- Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
- Write the summary in the imperative mood, lower case, no trailing period.
- Keep each commit focused on one change.

## Pull requests
- The title follows the commit message format.
- The description explains what changed and why, and contains `Closes #n` for the issue it delivers.
- Open the pull request early and request a review from the other team member.
- Every pull request needs one approval; resolve all review conversations before merging.
- The author merges the pull request and deletes the branch.

## Reviews
- Read the diff and run the change locally when you can.
- Use "Request changes" for problems that must be fixed, and suggested changes for small edits.
- Approve only when you are happy for the change to reach `main`.

## Keeping secrets and junk out
- Never commit secrets such as `.env` files or API keys.
- Generated files (`__pycache__/`, `*.pyc`, `*.log`, `tasks.json`) are ignored via `.gitignore`.
