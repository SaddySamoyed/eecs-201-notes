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

## 第二题: delete 了一个 branch 导致一个 commit 因为 poor rebase 被删除了, recover 这个 commit

这里要 recover 这个 commit，指要么 move HEAD 到 lost commit，要么能够 identify 它的 hash 值.

```shell
git branch recovery $(git reflog | grep 'rebase' | head -n 1 | awk '{print $1}')
```





## 第三题：恢复被 `git reset --hard` 删除的 changes

`git add my_file` stages a file, but it isn’t actually committed until you run git commit.
Sometimes you change your mind after a git add and run `git reset my_file` to unstage a file. The changes to that file are still there, however. To **really undo changes**, you use `git reset --hard` (or `git restore` or `git checkout`).

It can be a little too easy to accidentally type the wrongthing. 

In this repository, someone accidentally typed `git reset --hard` when they meant to just type `git reset`.

Fortunately, because they had already run `git add` to stage their changes, the deleted changes can be recovered.

Q1: 用什么指令来 recover initially staged contents?



Q2: What is the output of running `$ ./main`
