[TOC]

# Git1-Basic

## 1 预备工作

1. 连接服务器

```shell
ssh rynnefan@peritia.eecs.umich.edu
```

2. 获取代码

```shell
wget https://www.eecs.umich.edu/courses/eecs201/wn2024/files/assignments/basic-git1.tar.gz
```

3. 解压

```shell
tar xzf basic-git1.tar.gz
```

4. 进入子目录

```shell
cd basic-git1/calculator
```

## 2 working directory 描述

### 1. `inc`

`calc.h`

```c
#ifndef __CALC_H__
#define __CALC_H__

#ifdef __cplusplus
extern "C" {
#endif

enum op
{
    OP_ADD,
    OP_SUB,
    OP_MUL,
    OP_DIV
};

enum status
{
    STATUS_OKAY,
    STATUS_UNSUPPORTED,
    STATUS_DIV_BY_ZERO
};

enum status calculate(int arg1, int arg2, enum op op, int *re\
sult);

const char *op_to_string(enum op op);

#ifdef __cplusplus
```

### 2 `src`

包含两个文件 `calc.c`, `main.c`

1. `calc.c`

```c
#include "calc.h"

const char *op_to_string(enum op op)
{
#define _(x) case(OP_##x): return #x;
    switch (op) {
    _(ADD)
    _(SUB)
    _(MUL)
    _(DIV)
    default: return "(unknown op)";
    }
#undef _
}

enum status calculate(int arg1, int arg2, enum op op, int *result)
{
    switch(op) {
    case OP_ADD:
        *result = arg1 + arg2;
        return STATUS_OKAY;
    case OP_SUB:
        *result = arg1 - arg2;
        return STATUS_OKAY;
    // Issue #149: add support for mult
    case OP_DIV:
        // Issue #221: handle div by 0
        *result = arg1 / arg2;
        return STATUS_OKAY;
    }
    return STATUS_UNSUPPORTED;
}
```

2. `main.c`

```c
#include <stdio.h>
#include <string.h>

#include "calc.h"

int main(int argc, char *argv[])
{
    if (argc < 4) {
        printf(
        "calculate v0.9\n"
        "usage: <int 1> <operator> <int 2>\n"
        "\n"
        "operators:\n"
        "  + addition\n"
        "  - subtraction\n"
        "  x multiplication\n"
        "  / division\n"
        "\n"
        "return codes:\n"
        "  0: success\n"
        "  1: insufficient arguments\n"
        "  2: integer parse error\n"
        "  3: unrecognized operator\n"
        "  4: unsupported operator\n"
        "  5: divide by 0\n"
        );
        return 1;
    }

    // parse
    //  parse int
    int arg1, arg2;
    enum op op;

    int fail_parse = 0;
    if (sscanf(argv[1], "%d", &arg1) == 0) {
        fprintf(stderr, "int 1 (arg 1) is not an integer: '%s'\n", argv[1]);
        fail_parse = 1;
        return 2;
    }
    if (sscanf(argv[3], "%d", &arg2) == 0) {
        fprintf(stderr, "int 2 (arg 3) is not an integer: '%s'\n", argv[3]);
        fail_parse = 1;
    }
    if (fail_parse) return 2;

    //   parse op
    if (!strcmp(argv[2], "+")) {
        op = OP_ADD;
    } else if (!strcmp(argv[2], "-")) {
        op = OP_SUB;
    } else if (!strcmp(argv[2], "x")) {
        op = OP_MUL;
    } else if (!strcmp(argv[2], "/")) {
        op = OP_DIV;
    } else {
        fprintf(stderr, "operator (arg 2) '%s' not recognized\n", argv[2]);
        return 3;
    }

    // calculate
    int output;
    enum status status = calculate(arg1, arg2, op, &output);

    switch (status) {
    case STATUS_OKAY:
        printf("%d\n", output);
        return 0;
    case STATUS_UNSUPPORTED:
        fprintf(stderr, "Unsupported operation: %s\n", op_to_string(op));
        return 4;
    // Issue #221: handle div by 0
    }

    return 255;
}
```

### 3. Makefile

```makefile
File Edit Options Buffers Tools Makefile Help
CC=gcc
LD=ld
CFLAGS=-g

SRCDIR=src
INCLUDE=inc
OBJDIR=obj

SOURCES=$(wildcard $(SRCDIR)/*.c)
OBJECTS=$(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)
BIN=calculate

$(OBJDIR)/%.o:$(SRCDIR)/%.c
        mkdir -p $(@D) # generate the directory
        $(CC) $(CFLAGS) -I $(INCLUDE) -c $< -o $(@)

$(BIN): $(OBJECTS)
        $(CC) $(CFLAGS) -I $(INCLUDE) -o $(BIN) $(OBJECTS)

all: $(BIN)

clean:
        rm -rf $(BIN) $(OBJDIR)

.PHONY: all clean
```

## 3 git 操作

1. `git init`
2. `git add .`
3. 从 commit 中去除 binary 文件

```shell
git reset calculate
git reset obj/
```

`obj/` 表示 `obj` 目录下所有文件

4. `git commit -m "Initial commit"`
5. 添加 `.gitignore` 文件来自动忽略这些 binary 文件

```shell
emacs .gitignore
```

​     .gitignore 的内容就是 list of ignored files

```.gitignore
calculate
/obj
```

6. commit `.gitignore`

```shell
git add .gitignore
git commit -m "Add .gitignore"
```

7. 清除 binary 文件. `make clean`
8. 添加 README 说明一下这个东西怎么用. 然后 commit 这个文件.

```shell
git add README
git commit -m "Add README"
```

## 4 Branching

1. 添加两个branch

```shell
git branch issue149
git branch issue221
```

<img src="201-Hw2-assets\image-20240204214609994.png" alt="image-20240204214609994" style="zoom:50%;" />

2. switch 到 branch issue149 

```shell
git switch issue149
```

3. 更改一点代码，然后重新 make，然后 run 一下 binary 检验一下. 然后试试 `git diff`.

4. 使用 `git add -u` 来添加你修改过的文件.

5. `git commit -m "Implement multiplication"`

   <img src="201-Hw2-assets\image-20240204214929205.png" alt="image-20240204214929205" style="zoom:50%;" />

6. 到另一个 branch issue221，修改更多文件. 然后 commit.

   <img src="201-Hw2-assets\image-20240204215023743.png" alt="image-20240204215023743" style="zoom:50%;" />

7. 现在 `git switch master`.

8. merge 掉 `issue149`.

```shell
git merge issue149
```

Note that `issue149` and `master` have not diverged, making this process painless. This is known as **fast-forwarding**, where a branch just moves its pointer up to where another branch is.

<img src="201-Hw2-assets\image-20240204215047845.png" alt="image-20240204215047845" style="zoom:50%;" />

9. 现在 merge `issue221`.

   主要到这里 `master` 已经在 `issue 221` 的父节点前面的一个位置了，也就是说发生了 diverge.

   This will necessitate a special merge commit that gets automatically generated (which you don’t have to reword for this assignment). If the merge has to stop due to not being automatically resolved, use git status to see where the merge conflict is occurring and modify the files toget them into working order (i.e. it compiles and runs as intended for that branch), then complete the merge
   ( git status will give you instructions on how to do this).

## 5 Remote

1. 在 Gitlab 创建一个账号并添加和用于这个服务器一样的 ssh. 
2. 创建一个新的 private project.
3. 添加这个 gitlab 上的 project 为我们刚刚 directory 的 remote origin.

4. push 我们当前 branch 上所有 commits 到 remote.

```shell
git push -u origin --all
```

## 6 GitLab 提交

1. 在服务器里 gen 一个 ssh，然后加到 GitLab 账号里.

2. 然后创建一个 project: `eecs201-basic-git1.git`

3. 然后把它添加为我们这个 local repo 的 origin.

```shell
git remote add origin git@gitlab.eecs.umich.edu:rynnefan/eecs201-basic-git1.git 
```

4. 把我们本地所有 branch 的 所有 commits push 到 remote:

```shell
git push -u origin --all
```

5. 在 server 跑一下作业看看结果.

```shell
eecs201-test basic-git1
```

all pass！
