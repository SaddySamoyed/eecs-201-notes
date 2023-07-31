# Git & Github

[TOC]

家人们好, 今天我们来讲Git和Github. 没什么前言好说的, ~~因为我在正经学之前压根也不会.~~

## 1.1 Git and Version Control System(VCS)

Git是一款**分布式版本控制系统(Distributed Version Control Systems)**. 

我们写代码的时候, 我们希望保存源代码的不同版本, 这样当出现bug时我们可以回溯到之前的版本; 多人分工协作时, 我们可能需要和别人一起修改相同的文件, 我们希望有一个工具帮我们完成修改的合并, 节省很多时间.

那么**版本控制系统(VCS)**就是做这两件事情了. 一旦项目规模大起来, 我们就不得不用版本控制系统了. **Git**就是众多版本控制系统中的一种, 其他版本控制系统有例如CVS, Subversion, Mecurial, Perforce, Bazaar等比较知名. 它们应用的领域稍有不同, **Git是其中应用最广泛并且最适合中小项目开发的系统之一, 很适合入门**. 

Git本身也是一款**命令行工具**. 可能很多人更加推崇使用命令行工具而不是图形化工具, 因为命令行更适合写脚本, 自动化; 而图形化工具的操作更加直观. 

## 1.2 Client 

GitKraken是一款图形化客户端, 支持主流操作系统, 界面好看, 功能全面, 但现在已经收费了, 一个月4刀, 有点小贵. 

Git Bash是Git自带的Client, 非图形化, 非常fundamental但是有一点点麻烦.

Github Desktop是笔者认为的神中神, 不仅功能齐全, UI好看, 图形化和非图形化指令都支持, 而且免费. 虽然版本回顾没有GitKraken这么美观但是免费以及Github直连实在太香了.

综上笔者选择用Github Desktop作为Git的客户端.

## 1.3 Repository(repo)

repository就是**仓库**的意思, 指的是与项目相关的所有文件, 包括**源代码, 工程文件, 资源文件和一些配置信息**, 可以是**本地**的, 也可以是保存在**远程服务器**上的仓库. 

仓库之间可以相互同步, 比如可以把本地计算机上的代码同步到远程的服务器上. 

## 1.4 Github

Github上有很多远程代码仓库. 是当今最大的代码托管网站和开源社区. 

在Github Desktop创建repository时, 我们填写local(本机)位置, 就是在这台电脑上放在什么文件夹上. 创建repository时, 我们同时创建了一个在Github上的代码仓库.

## 1.5 Private and Public

**在Github网站上创建的仓库默认为private, 只有自己访问其中的代码和文件.**

那怎么设置为public, 即把项目open source呢?

1. 只有属于自己的仓库才能设置, 包括我们fork的属于别人的仓库. 首先进入拥有所有权的Github主页, 来到要操作的repository, 点击Settings.

2. 进入仓库的设置界面之后, 滑动到页面最底端, 找到Danger Zone

3. 找到change repository visibility按钮, 点击改为public.


## 1.6 Transfer ownership

同样在Danger Zone中, 可以把自己的repository的所有权让给别人. 

就这样, 然后就结束了(雾). 涉及到团队协作创作的其他问题, 当下还不用关心, 毕竟还没有团队, 用不到(悲). 以后再更新这个文档

## 1.7 将本地更新同步到Github

repository命名并创建好之后, 就可以往里面加任何格式的文件了, 修改或者加入文件后, Github Desktop会显示并同步所有变化. 这个时候选择在Github Desktop的同一repository的页面就可以填写本次变化的Summary(required)和Description了, 然后commit to main并push(上传)这一变化, 就可以把本次版本更新传到Github的托管仓库去了. 

## 1.8 将Github上的更新同步到本地

进入Repository文件夹, 右键点击Git Bash Here, 输入git pull origin.
