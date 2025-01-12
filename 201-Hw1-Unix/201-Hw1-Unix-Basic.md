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

通过

```shell
ssh <username>@<domain>
```

可以用 ssh 连接远程服务器.

比如我连接 peritia 的 eecs201 服务器 (注意在校外要开 umvpn-all traffic):

```shell
ssh rynnefan@peritia.eecs.umich.edu
```

连接上之后作业第一题:
```shell
uname -r
# 结果: 5.15.0-56-generic
```

# 3 Reading

https://www.joelonsoftware.com/2003/12/14/biculturalism/

现在，Windows 和 Unix 在功能上的相似性已经超过了差异性。从命令行、图形用户界面到网络服务器，它们都支持相同的主要编程隐喻；从几乎相同的文件系统、内存到套接字、进程和线程，它们都围绕着几乎相同的系统资源进行组织。每个操作系统提供的核心服务并没有太多限制你可以创建的应用程序种类。

剩下的就是文化差异了。Unix 和 Windows 程序员之间的文化差异是什么？这其中有很多细节和微妙之处，但大多数情况下归结为一点：Unix 文化重视**对程序员有用的代码**，而 Windows 文化重视**对非程序员有用的代码**。

这当然是一种重大的简化，但实际上，这就是最大的区别：我们是为程序员编程，还是为最终用户编程？其他一切都是评论。

让我们来看一个小例子。Unix 编程文化非常推崇可以从命令行调用的程序，这些程序可以使用参数来控制其行为的方方面面，其输出可以是格式规范、机器可读的纯文本。这类程序之所以受到重视，是因为程序员可以很容易地将其整合到其他程序或更大的软件系统中。举个微不足道的例子，Unix 文化中有一个核心价值观，雷蒙德称之为 "**沉默是金**"，即一个程序如果成功完成了你让它做的事情，就不应该提供任何输出。不管你是输入了 300 个字符的命令行来创建文件系统，还是构建并安装了一个复杂的软件，抑或是将载人火箭送上了月球。**如果它成功了，公认的做法就是什么也不输出**。用户会从下一个命令提示符中推断出一切正常。

这在 Unix 文化中是一个重要的价值观，因为你是在为其他程序员编程。正如雷蒙德所说，"胡言乱语的程序往往无法与其他程序很好地合作"。相比之下，在 Windows 文化中，你是在为玛吉阿姨编程，玛吉阿姨可能有理由认为，一个因为成功而没有输出的程序，与一个因为严重失败而没有输出的程序，或者一个因为误解了你的请求而没有输出的程序，是无法区分的。

同样，Unix 文化欣赏保持文本形式的程序。他们不太喜欢图形用户界面，除非在文本程序上干净利落地涂上口红，他们也不喜欢二进制文件格式。这是因为文本界面比图形用户界面更容易编程，而图形用户界面几乎不可能编程，除非有其他规定，比如内置脚本语言。在这里，我们再次看到，Unix 文化重视创建对其他程序员有用的代码，而这在 Windows 编程中很少成为目标。

这并不是说所有的 Unix 程序都是专为程序员设计的。远非如此。但是，Unix 文化重视对程序员有用的东西，这就说明了一两件事。

Windows 程序员中有一个重要的群体，他们主要是为其他程序员编码：微软内部的 Windows 团队。他们的工作方式是创建一个可通过 C 语言调用的应用程序接口（API）来实现功能，然后创建调用该应用程序接口的图形用户界面应用程序。你可以在 Windows 用户界面上做的任何事情，也可以通过使用任何合理的编程语言调用编程接口来实现。例如，微软 Internet Explorer 本身只不过是一个 89 KB 的小程序，它封装了几十个功能非常强大的组件，这些组件可以免费提供给成熟的 Windows 程序员，而且大多设计得非常灵活和强大。遗憾的是，由于程序员无法获得这些组件的源代码，因此只能按照微软的组件开发人员精确预见和允许的方式使用它们，而这并不总是可行的。有时还会出现错误，通常是调用 API 的人的过错，没有源代码就很难甚至不可能调试。

源代码可见的 Unix 文化价值使其成为一个更容易开发的环境。任何一位 Windows 开发人员都会告诉你，他们曾花了四天时间来追踪一个错误，原因是他们认为 LocalSize 返回的内存大小与他们最初使用 LocalAlloc 请求的内存大小相同，或者类似的错误，如果他们能看到库的源代码，十分钟就能搞定。雷蒙德发明了一个有趣的故事来说明这一点，使用过二进制形式库的人都会对此深有感触。

于是就有了这些宗教式的争论。Unix 更好，因为你可以调试库。Windows 更好，因为玛吉阿姨可以确认她的邮件是否真的发送出去了。实际上，两者并没有优劣之分，只是价值观不同而已：Unix 的核心价值观是让其他程序员更好地工作，而 Windows 的核心价值观是让玛吉阿姨更好地工作。

让我们看看另一种文化差异。雷蒙德说："经典的 Unix 文档写得简洁而完整......这种风格假定读者是积极的，能够推断出所讲内容的明显后果，并且有自信相信这些推断。仔细阅读每一个字，因为你很少会被重复告知任何事情"。他其实是在教年轻的程序员写更多不可能的手册。

对于最终用户来说，你永远也无法摆脱这种情况。雷蒙德可能会说这是 "过于简单化的居高临下"，但 Windows 文化深知最终用户不喜欢阅读，即使他们同意阅读你的文档，他们也只会阅读最少的内容，所以你必须反复解释......事实上，一个好的 Windows 帮助文件的特点是，任何一个单独的主题都能让普通读者自己读完，而无需假定他们了解其他任何帮助主题。

文化上的分裂是如此尖锐，以至于 Unix 从未在桌面上取得过任何进展。玛吉阿姨无法真正使用 Unix，而为 Unix 制作一个玛吉阿姨可以使用的漂亮前端的多次努力都以失败告终，这完全是因为这些努力都是由深受 Unix 文化熏陶的程序员完成的。这直接导致了用户界面的分裂；没有人能够就桌面用户界面应该如何工作的所有细节达成一致，他们认为这没有问题，因为他们的文化重视这种多样性，但对于玛吉阿姨来说，在一个程序中使用不同的用户界面进行剪切和粘贴，与在另一个程序中使用不同的用户界面是非常不妥的。因此，在 Unix 开发人员开始尝试在他们的系统上绘制良好的用户界面 20 年之后，我们仍然处于最大 Linux 供应商的首席执行官告诉人们家庭用户应该使用 Windows 的地步。我曾听经济学家说过，硅谷永远不可能在法国等地重现，因为法国文化对失败的惩罚太高，企业家们不愿意冒这个险。

也许 Linux 也是如此：它可能永远不会成为桌面操作系统，因为文化的价值取向阻碍了它的发展。OS X 就是最好的证明： 苹果公司最终为玛吉阿姨创造了 Unix，但这只是因为苹果公司的工程师和经理们坚定地信奉最终用户文化（我一直帝国主义地称之为 "Windows 文化"，尽管历史上它起源于苹果公司）。他们摒弃了 Unix 文化中以程序员为中心的基本准则。他们甚至重新命名了核心目录--异端！- 使用 "application "和 "library"等常用英语词汇，而不是 "bin "和 "lib"。

雷蒙德确实试图将 Unix 与其他操作系统进行比较和对比，但这确实是这本优秀著作中最薄弱的部分，因为他确实不知道自己在说什么。每当他开口谈论 Windows 时，都会显示出他对 Windows 编程的了解主要来自阅读报纸，而不是实际的 Windows 编程。没关系，他不是 Windows 程序员，我们可以原谅。对一种文化有深入了解的人通常都会这样，他知道自己的文化重视什么，却不太注意自己文化中普遍存在的部分（杀死老太太、程序崩溃：总是不好的）与只适用于为程序员编程时的部分（吃生鱼、命令行参数：取决于听众）之间的区别。

有太多文化单一的程序员，就像从未离开过明尼苏达州圣保罗市的典型美国孩子一样，分不清文化价值和人类核心价值之间的区别。我遇到过太多对 Windows 编程嗤之以鼻的 Unix 程序员，他们认为 Windows 是异教徒，是愚蠢的。雷蒙德经常掉进贬低其他文化价值观的陷阱，而不考虑这些价值观从何而来。在 Windows 程序员中很少发现这种偏执，因为总体而言，Windows 程序员都是以解决方案为导向的，没有意识形态偏见。至少，Windows 程序员会承认他们的文化存在缺陷，并实事求是地说："听着，如果你想把文字处理器卖给很多人，它就必须在他们的电脑上运行，如果这意味着我们要使用邪恶的注册表而不是优雅的 ~/.rc 文件来存储我们的设置，那就这样吧。Unix世界充满了自以为是的文化优越感、"倡导 "和Slashdot-karma-whoring宗派主义，而Windows世界则更加务实（"是啊，管它呢，我只是需要在这里谋生"），这一事实源于一种文化，它觉得自己受到了围攻，无法冲出服务器壁橱和业余爱好者市场，进入主流桌面。

这种软弱无力的傲慢是《UNIX 编程艺术》的最大缺陷，但这其实并不是什么大缺陷：总体而言，这本书对编程的许多方面都有令人难以置信的有趣见解，以至于我愿意在罕见的臭烘烘的意识形态咆哮中捏着鼻子，因为从书的其他部分可以学到许多关于普世理想的东西。事实上，我会向任何文化背景、任何平台、任何目标的开发者推荐这本书，因为它所宣扬的许多价值观都是普世的。当雷蒙德指出 CSV 格式不如/etc/passwd 格式时，他是在为 Unix 与 Windows 的竞争加分，但你知道吗？他是对的。/etc/passwd比CSV更容易解析，如果你读了这本书，你就会知道为什么，你也会成为一个更好的程序员。

Q: Has your computing experience thus far aligned more with “Windows culture” or “Unix culture”? What makes you feel that way? Do you feel that this blog post still holds up today, over 20 years since its publishing?

I personally aligned more with "Windows culture" so far. Though I do think that WSL for me is somehow indispensable, and commands do make it easy to program, I still think that the graphical commands of Windows are something I would use more. 

I think a big reason for this is that today there are many very well integrated and beautiful IDEs like VSCode. These include graphical debugging processes, graphical resource management systems, etc. I think it's true that Windows' graphical instructions are difficult to program with, but WSL's system makes up for this.  If programmers 20 years ago had to choose basically only one system to develop on, nowadays programmers can easily use virtual machines, dual systems, and most conveniently, sub-systems to assist in their development, so it's not the same thing as it used to be. So I think another important reason is that the developers of WIndows took some of the advantages of the *nix system and fused them into Windows. It's not one sided. Linux, as a prime example of a *nix system, also has a lot of great graphical desktop versions, like Ubantu Desktop. 

If I just want to look at a file, it takes me a few seconds to layer on a graphical folder, whereas if I want to type the `cd` command and the path it takes some typing and a lot more effort, so I'll definitely choose to use the mouse for the lightning bolt, and when I need to do something more computing, like make an `.exe` file I'll use the command line. 

I do think that the combination of a text editor and a shell is better for writing small files, but I can't do large projects without using a highly graphical IDE without getting burned out. As the author says, in Windows Aunt Marge makes it easy to know if my emails have been sent or not, and in a graphical IDE I can easily manage my project as a whole. Even if I might count as a programmer but not Aunt Marge, I would prefer this approach most of the time because it is intuitive.

Thus I don't think this article holds up completely by now, because the culture of operating systems is as much intertwined as the cultures of various nations today. For example, the author says that Linux will probably never be a desktop operating system, but now there are already a lot of linux desktop systems.
