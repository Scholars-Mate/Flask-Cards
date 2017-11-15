# How to Commit

## Keep your master branch up-to-date with GitHub

Don't make any commits on your master branch. Keep it up to date with the master
branch on GitHub:

Make sure you are on the master branch
```
git checkout master
```

Download everything off GitHub
```
git fetch
```

Update your branch to the current master branch from GitHub
```
git pull
```

## Do all your work in a separate branch

If you are doing any work, it should be in a separate branch:

Make your new branch based off your up-to-date master branch
```
git checkout master
```

Create a new branch. This command creates a new branch, then checks it out for
you
```
git checkout -b your-branch-name
```

Now you need to create the branch on GitHub. This command creates the branch on
GitHub and sets your branch to track it
```
git push -u origin your-branch-name
```

Use a descriptive branch name such as "front-end/login-page"

Do all of your work for this feature in this branch. All the commits in this
branch should be related to the feature/bugfix you are working on. If you want
to work on another feature, make another branch. Make sure that your commit
messages are descriptive. [HAAAAAAAAANDS](https://xkcd.com/1296/) is not a
descriptive commit message

## Ready to push your work to the master branch?

The master branch might have changed since you started your work. We want to
rebase our work on top of the new work that has been done:

Download everything from GitHub
```
git fetch
```

Rebase our work on top of the latest master branch. Note that you may have to
take care of merge conflicts
```
git rebase origin/master
```

Because you have rewritten history, you have diverged from you branch on GitHub.
You will need to force push your changes to your branch:
```
git push -f
```

After that, make a pull request with your branch. The pull request (and thus
your branch and all of its commits) should add an entire feature, fix a bug,
etc. Pull requests will need to be reviewed before they can be added. After they
are reviewed, don't forget to merge them, e.g. the "Rebase and merge" button.
