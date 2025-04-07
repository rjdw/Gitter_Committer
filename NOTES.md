# Thinking outloud

## Current Task
- How to get changes from pulled branch 

## Thought Process
- User Git Pull
- Changes from Github main branch 
Usually when you pull you get the summary of the changes in terminal
- What i need to do is get this summary, this info might be helpful to get the filenames of what changes, not sure it it shows u the lines changed directly. Testing out now

## What terminal looks like 

### Normal 
$ git pull origin master
From https://github.com/rjdw/Gitter_Committer
 * branch            master     -> FETCH_HEAD
Updating ff56766..fe35bb8
Fast-forward
 src/test/scrapfile.txt | 1 +
 test/scrapfile.txt     | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 src/test/scrapfile.txt
 create mode 100644 test/scrapfile.txt

### Merge Conflicts
$ git pull origin testing-pull-request 
From https://github.com/rjdw/Gitter_Committer
 * branch            testing-pull-request -> FETCH_HEAD
Auto-merging test/scrapfile.txt
CONFLICT (content): Merge conflict in test/scrapfile.txt
Automatic merge failed; fix conflicts and then commit the result.

Makes you fix merge conflicts first on the files directly 

 ## Useful commands

git diff HEAD@{1} HEAD: This compares your current HEAD (after the pull) with the previous HEAD (before the pull).