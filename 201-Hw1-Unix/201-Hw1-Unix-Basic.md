# 201-Hw1-Unix-Basic Notes

## 1 文件操作

从 WSL access windows files `/mnt/c/..`

删除文件：`rm somefile`

删除 directory: `rmdir somedir`

展示包括 hidden files 的所有内容: `ls -a`

展示某个 directory 的内容: `ls ...`

## 2 Course Server 和 SSH

SSH 也就是 Secure Shell，是一个 **protocol allowing for secure connections to another system**.

在许多系统中，不能简单地输入用户名和密码。取而代之的利用 SSH key.

它们以一对形式创建，一个 **private key** 和一个 **public key**，分别用于你要连接的每个系统（例如，我有多台计算机，所以我为它们生成了一对私钥和一对公钥.) 

private key 是你保存在本地机器上，不对他人公开，它用来验证你的身份. 

而你要访问的 server（例如 GitHub 或 class server）会与你共享 public key，并且它们会为你的账户保存公钥. 当你尝试访问 server 时，他们会向你的电脑发送用你的公钥加密的信息，你的电脑使用private key 对信息进行解密，如果解密后的信息与你的信息相符，你就通过了验证.

可以与多个 server 共享一个公钥：例如将笔记本电脑的 public key 用于 GitHub, GitLab, 实验室的服务器等，这样就可以通过笔记本电脑访问它们.

### 2.1 创建 SSH key

创建 keypair 的命令是 `ssh-keygen`.

有一些 additional options:

1. `-t <key type>`: 选择 要创建的 ssh key 的类型.  **The recommended type nowadays is `ed25519`, which
   is smaller, faster, and more secure than the old RSA keys.**
2. `-C <comment>`: 比如 `<username>@<hostname>` ，用来 help identify this key，尤其是有多个 computer 时，用来 keep track of which public key belonging to which of my
   several computers.

所以一个例子就是：

```shell
ssh-keygen -t ed25519 -C brandon@mydesktop
```

生成结束之后，进入 home directory 下的 `.ssh` 可以看到我们新创建的 `keypair`.

```shell
cd /.ssh
```

使用 `cat` 命令可以打印你的 key. 比如打印你的 public key:

```shell
cat id_ed25519.pub 
```

你会获得像这样的一个key:

```shell
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPLe4kBJcjpwnf3yq4/8aKop3MH brandon@celeritas
```

注意前面的 ssh-ed25519 也是一部分.

## 2.2 EECS201 的 Course Server

