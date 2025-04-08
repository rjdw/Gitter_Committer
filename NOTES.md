# Thinking outloud

## Current Task
- Get an LLM and make a wrapper for it

## Thought Process
- Browse models online, find free one
- just try and get something to work: generate summary
- Focus on finetuning later
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

$ git pull origin testing-pull-request 
From https://github.com/rjdw/Gitter_Committer
 * branch            testing-pull-request -> FETCH_HEAD
Merge made by the 'ort' strategy.
 test/scrapfile.txt | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)

### Merge Conflicts
$ git pull origin testing-pull-request 
From https://github.com/rjdw/Gitter_Committer
 * branch            testing-pull-request -> FETCH_HEAD
Auto-merging test/scrapfile.txt
CONFLICT (content): Merge conflict in test/scrapfile.txt
Automatic merge failed; fix conflicts and then commit the result.

Makes you fix merge conflicts first on the files directly 

 ## Useful commands

git diff HEAD@{1} HEAD: This compares your current HEAD (after the pull) with the previous HEAD (before the pull).'

## Results
Just run git diff HEAD@{1} HEAD. I think we can just have a flag to be added to get_git_diff function

## TODO
- Write function to parse through git diff and get the function names
- Make a Tree of important imports for changed files 
- Test with more complex diffs. Its super generic. Prob prompt it better
