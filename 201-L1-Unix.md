[TOC]

# 1 Unix, Command Structure and commands

## 1.1 *nix systems

**"*nix (类Unix系统)"** refers to **a group of operating systems** derived from 或 inspired by Unix OS (Unix 由 AT&T Bell Labs 开发).

*nix OS 会 follow similar principles and provide similar (software) interfaces

GNU/Linux 和 MacOS 都是 *nix OS，而 Windows 则不是.

但是 Windows 有内置的 WSL (subsystem for Linux)，是 *nix. 并且WSL2已经使用了真正的 linux kernal.

## 1.2 Command Line & Shell

**Command Line** 是一种 **Interface**，在这个 interface 里你提供 text，而它的 interpreting software 会把你的 text 翻译成 commands 来执行.

这个 interpreting software 就叫做 **shell**.

过去我们使用 video terminal devices，而今天我们不用了. 但是我们现在使用 **virtual terminals** and **terminal emulators** to act like them (e.g. macOS Terminal, iTerm
2, Command Prompt)

除了使用 Text 作为 input 的 shell 外，也有 **Graphical shells**，也就是我们平时用的 Windows 和 macOS 的 GUI. 这些 GUI 通过获取你的鼠标对 shortcut 的点击作为 input，然后翻译成 command，来打开一些 applications.

GUI 很难 automate，但是 text 可以，所以更加灵活一些.

我们接下来将用 shell 这个词指代 *nix command line shell. 

**不论你使用的是什么 shell (zsh, bash, ...)，它都 follow similar syntax！**

在 shell 中你可以：

1. navigate through directories
2. modify files
3. launch apps

**大多数 shell 会支持 tab completion，也就是说 Tab 键可以让 shell 智能完成一句写了一半的话（写得肯定不一定对）**

### 1.2.1 Command structure

```shell
<command> <argument 1> <argument 2> <argument 3>
```

<img src="Assets\image-20240129231624439.png" alt="image-20240129231624439" style="zoom: 67%;" />

1. 每个组成之间由空格分开.
2. 有些命令是 shell 的 built-in，有些命令就是程序名
3. 在 command 的左侧这个 `$` 是 shell 自带的，它叫做 **prompt.**

## 1.3 *nix 的 Filesystem

*nix system 的 Filesystem 都有下面的特点.

1. 我们可以 address and locate files via **"paths(路径)"**

2. 每个 running program **包括 shell 本身** 都有一个 **current working directory(当前工作目录)**.

3. 使用 `/` 来 enter 及 separate directories.

4. 用 `.` 指代当前 directory，`.. `指代父目录.

5. 使用 `/` 开始表示 absolute path，而使用 `./dir1/dir2`，`../../some-dir`，`dir1/dir2` 等来表示 relative directory.

6. common pattern: 

   ```shell
   <command> <path-to-file>
   ```

   比如:

   ```shell
   nano 1.txt
   ```

   ```shell
   vim 1.cpp
   ```

# 1.4 *nix 系统常用 commands

### 1.4.1 基础 commands

| command |                        usage                        |
| :-----: | :-------------------------------------------------: |
|   man   |       "manual pages": gives info on programs        |
|   pwd   |               print working directory               |
|   ls    |          lists the contents of a directory          |
|   mv    |     移动文件到另一个 directory 或者 rename 文件     |
|   cd    | changes your current directory (到后面的 arguments) |
|  touch  |    创造空文件或更新 timestamp (如果该文件已存在)    |
|   rm    |                      删除文件                       |
|  grep   |                   搜索文件或数据                    |
|   cat   |    concatenate：连接多个文件，也用来打印文件内容    |
|   cp    |                    copy 文件(s)                     |
|  wc -l  |               count input 文件的行数                |

更多命令：https://en.wikipedia.org/wiki/List_of_POSIX_commands

可以使用 `--help` 来获取一个命令如何用的信息. 比如：

```shell
cat --help
```

### 1.4.2 操作各种 output，从 cmd output 到文件

1. 把一个 command 的输出结果 (或者一段文字) 输送到另一个 command 作为输入，符号是一个 **pipe (`|`)**：

   ```shell
   echo cmd1 | cmd2
   # cmd1 的输出, 输送到 cmd2 作为输入.
   ```

   比如:

   ```shell
   echo "hello world" | rev
   ```

2. 把一个 command 的 output 或者一段文字输送进一个 file，符号是一个 **output redirection (`>`)**：

   ```shell
   echo "hello world" > some-file
   ```

3. retrieve 一个 file 作为 input，输送到一个 command，符号是一个 **input redirection (`<`)**：

   ```shell
   rev < some-other-file
   ```

### 1.4.3 Intro to automation

你可以把一系列 commands 放进一个文件，叫做一个 **script(脚本)**.

现在，只要将 filename 作为 shell 的参数，就可以随时运行该脚本.

```shell
bash myscriptfile
```

如果你的 script 被标记为 executable，还可以直接 Invoke 它作为一个 program.

```shell
./myscriptfile
```



