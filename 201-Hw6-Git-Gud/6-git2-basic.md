# Git2 basic hw

## 1 Cloning and changing a remote

```shell
git clone git@gitlab.eecs.umich.edu:eecs201/eecs201-basic-git2.git
```

Clone 完成

```shell
cd eecs201-basic-git2
```

We’re going to make a local version of every remote branch.

```
for branch in $(git branch -a | grep "remotes/origin" | grep -v "HEAD" | sed -e "s:remotes/origin/::");
do
	git switch "$branch";
done
```

By default when you clone a remote called `origin` will created and its URL will be set to where you cloned it from. We’ll need to change the URL of `origin` to point to your project, and then push all the branches to it.

```shell
# set the url for a remote
git remote set-url origin git@gitlab.eecs.umich.edu:rynnefan/eecs201-basic-git2.git

# push all branches to the remote and set the remote branches as upstreams
git push -u origin --all
```

This assignment has a decent amount of room for error. You might want to create local “backups” of the branches that you can `git reset --hard` to in case you mess up.

```shell
# think about what this does and how it works
for branch in $(git branch | cut -c 3-);
do
	git tag "backup-$branch" "$branch";
done
```

This will something known as a “tag” of each branch called `backup-<branch name>` . These tags are named references that point to commits, so you can use them as backup references to get back to a particular state with `git reset` . For example, if you’ve completely messed up dev , you can use `git reset --hard backup-dev` to move `HEAD` to where `backup-dev` is (which is where `dev` was at the beginning of the assignment).
There are two feature branches: `bug-space-stdout` and `feat-spongebob` . We’ll be looking at both of them in the assignment. In this assignment, the main branch is `dev` . You’ll be pushing the final changes to `origin/dev`.

## 2 Merge conflict

In this question we’ll be merging in a branch that will cause a merge conflict: the `bug-space-stdout` feature branch into `dev`. In this situation, `bug-space-stdout` branched off from `dev` and then `dev` had another commit pushed to it, so a divergence point has formed. What `bug-space-stdout` ’s new commit does is fix `space.cpp` so that it outputs to standard output instead of standard error. What `dev` ’s new commit does is replace the use of C `stdio` calls (e.g. `printf` ) with C++ `iostream` calls (e.g. `cout <<` ).

1. Switch to the `dev` local branch.
2. Run `make` to build the application that the repo is versioning. If you want to, play around with it by running `./memetext space 'Hello world!' ` or with whatever string you want.
3. Run `git merge bug-space-stdout` to merge `bug-space-stdout` into the current branch (`dev`).
4. This will cause a merge conflict. The merging process will stop for you to deal with the files that have encountered merge conflicts. These files will have parts of them marked off that indicate what the conflicting commits are saying the file should have. These look like `<<<<<<<` and `>>>>>>>` , and are examples of “version control markers”.
5. Deal with the files in conflict. If you have trouble understanding what needs to be fixed, investigate the latest commit in `dev` and `bug-space-stdout` to see what their goals are. You can do this by using `git log` ,`git show`, and `git diff`.
e.g. `git show 5329d04` will show you what was added/removed in `dev` ’s commit. In the end, your fix for the merge conflict should reconcile the ideas in both commits: as a result of this merge, the conflicting part of `space.cpp` should use C++ iostreams to output to standard out (the error printout when not enough arguments are provided should still use standard error). e.g. `std::cout << "Some stuff" << std::endl` and not `printf("Some stuff\n")` This will involve removing the version control markers and the code reflecting the ideas in the two commits being merged together.
6. Make sure that the code is in compilable condition and that it works as intended. Try building and running the application again.
7. When you are done handling the conflict, stage the appropriate files to mark them as resolved and commit (If you run `git status` it will also communicate this step for you). A merge commit message will automatically be worded for you. This resulting merge commit will contain the changes you made to resolve the conflict as well as linking the divergen histories together.
8. Hooray! You have successfully dealt with a merge conflict!