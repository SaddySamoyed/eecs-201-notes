[TOC]

# 201-Hw2-Git1-Adv

下载文件.

```shell
wget https://www.eecs.umich.edu/courses/eecs201/wn2024/files/assignments/adv-git1.tar.gz
tar xzf basic-git1.tar.gz
```

## 第一题: 不使用 `git revert` 或者 `git reset` 就恢复文件到上一次 commit

题目：上一次 commit 删了所有的 `.png` 文件. 现在要恢复这些文件，并且不能使用 `git revert` 或者 `git reset`.

我的答案：

我们可以使用：

```shell
git checkout <commit-hash>^ -- <path-to-image>
```

来恢复.

而这里我们需要通过 `git log` 获取之前 commit 的哈希值.

但是如果只想获得前一次 commit (即最新 commit 的父 commit) 的哈希值，还有一种方法：

```shell
git rev-parse HEAD^
```

于是我们可以把这两个指令合成一个指令:

```shell
git checkout $(git rev-parse HEAD^) -- *.png
```

`$` 表示把一个指令的值嵌入外面的指令作为参数.

## 第二题: delete 了一个 branch 导致一个 commit 因为 poor rebase 被删除了, recover 这个 commitgit reflog

在 Git 中，如果你丢失了一条 commit，但知道这个 commit 曾经存在（即，它曾经被指向过，但现在没有任何分支或标签指向它），你仍然有机会恢复它。Git 保留了一个详细的日志，记录了你的 HEAD 和分支指针的变化。这个日志可以通过 `git reflog` 命令访问。使用这个命令，你可以找到丢失的 commit 的 hash，并将你的 HEAD 移动到该 commit 或者创建一个新的分支指向它.

首先，运行 `git reflog` 命令来查看你的 HEAD 和分支指针的变化历史：

```shell
git reflog
```

这个命令会列出你所有的 HEAD 变化，包括 commit 操作、checkout 操作等。每一条记录都会显示一个 commit 的 hash 和操作的描述.

然后，从这个列表中找到丢失的 commit 对应的条目. 

```shell
git show 53a98e0
```

如果你想将你的 HEAD 移动到这个丢失的 commit，使用以下命令:

```shell
git checkout 53a98e0
```

或者，如果你想创建一个新的分支来指向这个丢失的 commit，从而更安全地恢复它，可以使用以下命令：

```shell
git branch recover-branch 53a98e0
```

然后，你可以切换到这个新创建的分支：

```shell
git checkout recover-branch
```

```shell
git checkout 53a98e0
```

## 第三题：恢复被 `git reset --hard` 删除的 changes

`git add my_file` stages a file, but it isn’t actually committed until you run git commit.
Sometimes you change your mind after a git add and run `git reset my_file` to unstage a file. The changes to that file are still there, however. To **really undo changes**, you use `git reset --hard` (or `git restore` or `git checkout`).

It can be a little too easy to accidentally type the wrongthing. 

In this repository, someone accidentally typed `git reset --hard` when they meant to just type `git reset`.

Fortunately, because they had already run `git add` to stage their changes, the deleted changes can be recovered.

Q1: 用什么指令来 recover initially staged contents?

```shell
git fsck --no-reflog --lost-found --unreachable HEAD
git show 245c2fb1070a22c01960cdd4d576cd472f25b779
git show 245c2fb1070a22c01960cdd4d576cd472f25b779 > main.c
```

Q2: What is the output of running `$ ./main`

```
The answer to life, the universe, and everything is the Oxford Comma
```

