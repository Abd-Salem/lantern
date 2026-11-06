# Evidence - Student B (Mostafa, zlatanibrahimovichsweden-61)

## E1 - Remotes (authentication: SSH)
```
$ git remote -v
origin  git@github.com:Abd-Salem/lantern.git (fetch)
origin  git@github.com:Abd-Salem/lantern.git (push)
```

## E3 - Two consecutive commits on main
Commits: dfd747b `feat(storage): add load() for tasks.json` and 08012a0 `feat(storage): add save() writing tasks.json`
```
$ git rev-parse HEAD~1 HEAD
dfd747b5bfe82b0a34e5973032711c1cae152df5
08012a0f47a72f72d177ed2739979fbb74c68ba4

$ git rev-parse "HEAD~1^{tree}" "HEAD^{tree}"
e8e9205616f9992e77d96ca52a106dcf2db4aa09
0c4e2fbb569e259ae751212b9c9abaac37f8d315

$ git ls-tree HEAD~1
100644 blob 16adcf72f34ec595c9cbbd222d77a90c007eec22    README.md
100644 blob 125caf1835bc9202b20dc7da098e2a9c47dddb71    lantern.py
100644 blob a7ef1e660dfefe34e60accdf8c94420fccfec6dc    storage.py
100644 blob ed7ffcb0c61755dff57d7ac5a2d537771c041679    tasks.py

$ git ls-tree HEAD
100644 blob 16adcf72f34ec595c9cbbd222d77a90c007eec22    README.md
100644 blob 125caf1835bc9202b20dc7da098e2a9c47dddb71    lantern.py
100644 blob 68016ab2d049114140eb0290a52ca4b18755ee2c    storage.py
100644 blob ed7ffcb0c61755dff57d7ac5a2d537771c041679    tasks.py
```
- Same blob in both commits: `README.md` -> 16adcf72f34ec595c9cbbd222d77a90c007eec22
- Different blob: `storage.py` -> a7ef1e660dfe... (dfd747b) vs 68016ab2d049... (08012a0)

## E4 - History graph after Requirement 3 merges
Fast-forward: ad6b17a (fix/stable-key-order). Merge commit with conflict resolved: 0b90075 (feature/pretty-json), resolved line `json.dump(tasks, f, indent=2, sort_keys=True)`.
```
$ git log --oneline --graph --all -6
*   0b90075 (HEAD -> main) Merge branch 'feature/pretty-json'
|\
| * c80d6b7 (feature/pretty-json) feat(storage): write JSON with an indent of 2
* | ad6b17a (fix/stable-key-order) fix(storage): write JSON keys in sorted order
|/
* ea5592e (origin/main, origin/HEAD) Rename draft.txt to notes.txt
* 1998998 Add draft.txt placeholder
* 6bea3b5 chore: remove scratch.txt placeholder
```

## E5 - Drill (b): commit made on the wrong branch
```
$ git commit -m "docs(usage): add Examples heading"
[main 4ca42e8] docs(usage): add Examples heading
$ git status -sb
## main...origin/main [ahead 1]
$ git branch docs/usage-heading
$ git reset --hard origin/main
HEAD is now at 417daca Merge branch 'main' of github.com:Abd-Salem/lantern
$ git rev-parse main origin/main
417daca491730e3cd313bc7109ac05ddef979d94
417daca491730e3cd313bc7109ac05ddef979d94
$ git reflog -6
417daca (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: reset: moving to origin/main
4ca42e8 (docs/usage-heading) HEAD@{1}: commit: docs(usage): add Examples heading
417daca (HEAD -> main, origin/main, origin/HEAD) HEAD@{2}: commit (merge): Merge branch 'main' of github.com:Abd-Salem/lantern
53d019c HEAD@{3}: commit: chore: untrack log and pycache, add .gitignore
5f1db51 HEAD@{4}: commit: chore: add lantern.log and __pycache__ (mistake)
0b90075 HEAD@{5}: reset: moving to HEAD~1
$ git merge --no-ff docs/usage-heading -m "Merge branch 'docs/usage-heading'"
$ git push origin main
   417daca..344966e  main -> main
$ git log --oneline --graph -4
*   344966e (HEAD -> main, origin/main, origin/HEAD) Merge branch 'docs/usage-heading'
|\
| * 4ca42e8 docs(usage): add Examples heading
|/
*   417daca Merge branch 'main' of github.com:Abd-Salem/lantern
```

## E6 - Stash parked and reapplied
Parking the unfinished list --sort work:
```
$ git stash push -m "wip: list --sort option"
Saved working directory and index state On feature/list-sort: wip: list --sort option
$ git stash list
stash@{0}: On feature/list-sort: wip: list --sort option
```
Reapplying after PR #4 was squash-merged (fa4365c):
```
$ git switch feature/list-sort
$ git merge main
Updating 82fb63e..fa4365c
Fast-forward
$ git stash list
stash@{0}: On feature/list-sort: wip: list --sort option
$ git stash pop
Dropped refs/stash@{0} (bfd44ae393106515ec24f8ad94b9a9d53d6887a0)
$ git stash list
$
```
