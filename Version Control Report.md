# Version Control
## What is version control?
Version control systems are a category of software tools that helps in recording changes made to files by keeping a track of modifications done in the code.Version control software helps automate this process.

## Why is Version control important?
A version control system is a kind of software that helps the developer team to efficiently communicate and manage all the changes that have been made to the source code along with the information like who made and what changes have been made.
A separate branch is created for every contributor who made the changes and the changes aren’t merged into the original source code unless all are analyzed as soon as the changes are given a green signal, they are merged to the main source code.
It not only keeps source code organized but also improves productivity by making the development process smooth.
Basically the Version control system keeps track of changes made on a particular software and takes a snapshot of every modification.
Let’s suppose if a team of developers add some new functionalities in an application and the updated version is not working properly so as the version control system keeps track of our work so with the help of version control system we can omit the new changes and continue with the previous version.

## Different types of version control.

### Local version control systems
It is one of the simplest forms and has a database that keeps all the changes to files under revision control. RCS is one of the most common VCS tools. It keeps patch sets (differences between files) in a special format on disk. By adding up all the patches it can then re-create what any file looked like at any point in time.

### Centralized version control systems
Centralized version control systems contain just one repository(storage location) globally and every user needs to commit to reflecting one’s changes in the repository. It is possible for others to see your changes by updating.
Two things are required to make your changes visible to others which are:   
 - You commit    
 - They update
      
The benefit of CVCS (Centralized Version Control Systems) is collaboration amongst developers along with providing an insight to a certain extent on what everyone else is doing on the project. It allows administrators to fine-grained control over who can do what. 
It has some downsides as well which led to the development of DVS. The most obvious is the single point of failure that the centralized repository represents if it goes down during that period collaboration and saving versioned changes is not possible. What if the hard disk of the central database becomes corrupted, and proper backups haven’t been kept? You lose absolutely everything.

### Distributed version control systems
Distributed version control systems contain multiple repositories. Each user has their own repository and working copy. Just committing your changes will not give others access to your changes. This is because commits will reflect those changes in your local repository and you need to push them in order to make them visible on the central repository. Similarly, When you update, you do not get others’ changes unless you have first pulled those changes into your repository. 
To make your changes visible to others, 4 things are required:  
 - You commit    
 - You push    
 - They pull    
 - They update
         
The most popular distributed version control systems are Git, and Mercurial. They help us overcome the problem of single point of failure


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
## clone command
The `git clone` is used create local copies of remote repositories.
But in 'Learn Git Branching' though -- `git clone` actually makes a remote repository out of your local one.

## fetch command
The `git fetch` is used to fetch data from a remote repository.    
It performs two main steps :
 - downloads the commits that the remote has but are missing from our local repository
 - updates where our remote branches point
git fetch usually talks to the remote repository through the Internet (via a protocol like http:// or git://).
It will not update your main branch or change anything about how your file system looks right now.

## pull command
`git pull` is essentially shorthand for a git fetch followed by a merge of whatever branch was just fetched.

## status command
The `git status` command gives us all the necessary information about the current branch. `git status` gives information about the branch & files
We can gather information like:
 - Whether the current branch is up to date
 - Whether there is anything to commit, push or pull
 - Whether there are files staged, unstaged or untracked
 - Whether there are files created, modified or deleted








'HEAD' is the symbolic name for the currently checked out commit
'o/main', the branch name is main and the name of the remote is o
