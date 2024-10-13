# Git Commands

## Commit command
The `git commit` command records snapshots of all the tracked files in your directory. Every time we make a commit, Git saves the current state of the files, creating a new version. Thus, Instead of copying the whole directory every time we make a commit, it tries to save space by recording just the changes, or "deltas," between these versions/states of the repository.
```
git commit
```

## Branching
Branching helps in dividing the work through small branches instead of having very big branches.    
We can checkout or access that particular branch throught the `git checkout` command.     
In Git version 2.23, a new command called `git switch` to replace the `git checkout` command but is still experimental.     
```
git branch branch_name
git checkout branch_name;
git commit
```

A shortcut to create and access a branch at the same time would be to do the following.
```
git checkout -b branch_name
```

## Merge command
The `git merge` command merges the specified branch into your current branch.
```
git merge branch_name
```


## Rebasing
Instead of creating a new merge commit, `git rebase` moves or combines a sequence of commits to a new base commit. It is used to move or apply your changes from one branch onto another branch.
```
git rebase branch_name
```

### Interactive Rebasing
Allows to rebase multiple commits at the same time.
```
git rebase -i HEAD~4
```


## Log command
The `git log` command is used to see hashes. It only requires you to specify enough characters of the hash until it uniquely identifies the commit.     
### Relative Reference
Moving upwards one commit at a time with `^`       
Moving upwards a number of times with `~<num>`     
We can can directly reassign a branch to a commit with the `-f` option.


## Revert/Reset command
The `git reset` command reverses changes by moving a branch reference backwards in time to an older commit.   
The `git revert` command is used to undo changes by creating a new commit that reverses the changes made by a previous commit.
```
git reset branch_name_to_be_reset_to
git revert branch_name_to_be_reverted_to
```

## cherry-pick command
It is used to copy a series of commits below your current location (HEAD).c
```
git cherry-pick <Commit1> <Commit2> <...>
```










'HEAD' is the symbolic name for the currently checked out commit
