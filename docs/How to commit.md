# How to Commit

## Do all your work in a separate branch

Create your own branch based off master

```
git checkout master
git checkout -b your-branch-name
git push -u origin your-branch-name
```

## Ready to commit?

Rebase your work on top of the latest master branch

```
git fetch
git rebase origin/master
git push -f
```

After that, make a pull request
