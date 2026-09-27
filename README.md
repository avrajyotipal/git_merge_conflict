# Git Merge Conflict Resolution Project

## Project Overview

This project demonstrates how Git handles merge conflicts when two branches modify the same line of the same file differently.

## Branches

- main
- feature-discount
- feature-premium-discount

## Workflow

1. Created the initial project on main.
2. Created feature-discount from main.
3. Changed the discount from 10% to 20%.
4. Committed the change.
5. Created feature-premium-discount from the original main branch.
6. Changed the discount from 10% to 30%.
7. Committed the change.
8. Merged feature-discount into main.
9. Attempted to merge feature-premium-discount.
10. Git generated a merge conflict.
11. Inspected Git's conflict markers.
12. Manually resolved the conflict.
13. Selected the 30% discount implementation.
14. Committed the conflict resolution.
15. Verified the final merged history.

## Git Commands Demonstrated

- git init
- git status
- git add
- git commit
- git branch
- git checkout
- git diff
- git merge
- git log --oneline --graph --all