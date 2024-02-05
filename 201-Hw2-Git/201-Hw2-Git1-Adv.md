# 201-Hw2-Git1-Adv

下载文件.

```shell
wget https://www.eecs.umich.edu/courses/eecs201/wn2024/files/assignments/adv-git1.tar.gz
tar xzf basic-git1.tar.gz
```

## 第一题: 不使用 `git revert` 或者 `git reset` 就恢复文件到上一次 commit

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

