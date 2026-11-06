# Evidence for Student A

## E1: Remotes and authentication (HTTPS)
```
origin	https://github.com/Abd-Salem/lantern.git (fetch)
origin	https://github.com/Abd-Salem/lantern.git (push)
```

## E2: Same file staged and not staged, two different diffs
```
$ git status
On branch docs/evidence-a
Your branch is up to date with 'origin/docs/evidence-a'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   notes.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	evidence/A.md

$ git diff
diff --git a/notes.txt b/notes.txt
index f60268a..6040c41 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1,3 +1,4 @@
 placeholder
 first line
 staged line
+unstaged line

$ git diff --staged
diff --git a/notes.txt b/notes.txt
index cb2ea67..f60268a 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1,2 +1,3 @@
 placeholder
 first line
+staged line
```

## E4: History after the Requirement 3 merges
```
*   863f55e Merge branch 'feature/done-flag'
|\  
| * 3d0c7f0 add a "done" : False field
* | ef54a7a Strip surrounding whitespace from the title
|/  
* ea5592e Rename draft.txt to notes.txt
* 1998998 Add draft.txt placeholder
* 6bea3b5 chore: remove scratch.txt placeholder
```

## E5: Reflog for the undo drills
Drill (a), message typo fixed with amend:
```
bdbcaac HEAD@{67}: commit (amend): Add first line notes.txt
3df9c1f HEAD@{68}: commit: Add first nte to notes.txt
```

Drill (c), lost commit discarded with a hard reset, then recovered:
```
bdbcaac HEAD@{61}: reset: moving to HEAD~1
f0e0943 HEAD@{62}: commit: Add another line to notes.txt
--
bdbcaac HEAD@{65}: reset: moving to HEAD~1
6e5b4bd HEAD@{66}: commit: Add another line to notes.txt
1fac4e1 HEAD@{2}: cherry-pick: Add another line to notes.txt
```

## E7: Rejected direct push to main
```
remote: error: GH013: Repository rule violations found for refs/heads/main.        
remote: Review all repository rules at https://github.com/Abd-Salem/lantern/rules?ref=refs%2Fheads%2Fmain        
remote: 
remote: - Changes must be made through a pull request.        
remote: 
To https://github.com/Abd-Salem/lantern.git
 ! [remote rejected] HEAD -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/Abd-Salem/lantern.git'
```
