'''
1.using version control toll we can work together in a shared folder on the same set of files.
2. keep historical record of changes in the repository for future purpose.

#  link to know abot version control tool: 

https://www.seguetech.com/a-review-of-software-version-control-systems-benefits-and-why-it-matters/

# link to Download a git -> 

https://git-scm.com/download/win

'''

# Creates a GIT repository copy from a remote source
git clone  url

# To know git status
git status

# Adds files changes in your working directory.
git add filename or directory

# Removes files from your working directory
git rm filename

# To commit local changes
git commit -m " commit message "

# Pushes all the modified local objects to the remote repository
git push

#  Fetches the  remote repository changes into local repository.
git pull

# Resets your working directory to the state of your last commit
git reset --hard origin/main

# To checkout REMOTE repository file
git checkout "note.py"


## Branch
# To list all branches 
git branch

# To create a new branch
git branch branchname

# Switched to branch "testing"
git checkout testing

# Deleted branch testing.
git branch -d testing



