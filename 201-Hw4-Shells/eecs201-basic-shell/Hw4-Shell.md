# Hw4-Shell

## 1 Expansion Fun

Write a shell script name `get-my-info` that:

1. Prints out `Login: <user name>`
2. Prints out `OS: <operating system>`
3. Prints out `hostname: <computer name>`
4. Prints out `<dir>'s device: <device space used/<total size> (<% used>) `. The dir will be provided as the first argument: if there is no first argument, defaults to `/` . This will print out usage stats about the device that the directory is on (not the directory’s actual usage).

Below are hints:

1. • You can get the username from the `logname` command
   • You can get the OS by running `uname -s`
   • You can get the computer’s name (“hostname”) by running `uname -n`

2. `echo` can print strings out for you: combine that with liberal use of command substitution to expand the output of a command and with quoting you can manage how you print things out. For example, you can run `echo "welcome $(echo "$HOME" | rev)"` : this will run `echo "$HOME" | rev` inside of a subshell, capture its output, and then substitute that into the `echo "welcome $(...)"` .

3. It gets more interesting when getting a directory’s device’s disk usage. `df -h <directory>` (e.g. `df -h /home/brandon` ) takes a directory, looks at what storage device that directory is on, and prints out some disk usage stats for that storage device (not the directory). 

4. When you run it, note how it prints out a line that labels what each column is: we want the data, not the column name. The `tail` command can help us here: it gets the last lines of output. Specifically, `tail -n 1` will get the last line of output. Remember pipes from the last assignment? They’re our ever-present friend :). Now we need to get our data: the `awk` utility can help us here. `awk '{print $1}'` will get the 1st field (column). Replace `1` with another number and you’d get that number’s field. 

   Putting this together, you can form a pipeline to grab fields of data from `df` ! You might find that handling these pipelines and expansions a bit cumbersome: feel free to declare variables to handle certain things, like one to hold the total disk space, one for the used disk space etc. On both Linux and macOS systems, the `Size` column represents the total size and the `Used` column represents the amount of space used. On Linux systems, the `Use%` column is the % of space used, and on macOS this is the `Capacity` column.

5. You might be wondering about the “default to `/` ” part: recall from class how there was a parameter/variable expansion that allows us to have a default expansion value when a variable is unset/doesn’t exist. For example `${hello:-world}` will try to expand the variable `hello` , but if `hello` has not been set/is undefined, it will expand out to the string `world` instead.
   Try to think of a way to take advantage of this with the potential existence of the first argument `1` . Perhaps you can have a variable that represents the what directory to look at, regardless of whether there’s an argument or not?

## 2 Control Flow

Write a shell script named `shebang-check` (no extension) that:

Checks if the first two bytes are `#!` , indicating a shebang. If there is one, print out the basename of the
file (filepath minus the directories i.e. the “name” of the file) and the interpreter used (i.e. the stuff after `#!` ): `filename: /path/to/interpreter` e.g. `some-script: /bin/sh`

The following bullets are cases for behavior involving this “check”

1. Case 1: there are no arguments.

   Iterates over every file in the current directory. If the file is a normal file, “check”s it, else, does nothing.

2. Case 2: there are arguments.

   Each argument represents a normal file or a directory. If the argument is a normal file, “checks” it. If the
   argument is a directory, iterates over each file in that directory and “checks” it if it is a normal file, else does nothing (just like the no argument case, but with a particular directory). There is no recursion here: with directory arguments, only check normal files inside of them and do not traverse subdirectories.

Note: In any case, the output is **sorted**.

Hints:

When you write your “check”, you might want to take advantage of the `test` / `[ ]` structure to check of the first two bytes of the file are indeed `#!` . You’ll probably need to take advantage of **command substitutions** like in the previous problem. Remember that you’re always free to declare variables when these substitutions begin to become more and more cumbersome!

For the main logic, you’ll need to check if there are variables in order to decide what to do. The big part of this is iteration: you’ll probably want to use a for -loop for this. Now the big question is how to get the list that you iterate over: if you want to try something new, you could try using a **filename expansion (glob/wildcard)** (e.g. `dir/*` ) to populate a list of files for you, or you could use the output of `ls` : your choice (though I do highly recommend filename expansion). Another neat thing about `test` / `[ ]` is that it can do more than binary comparisons: you can also check if files exist or if they’re normal files: `[ -f filepath ]` can check if a file is a normal file and `[ -d filepath ]` can check if a file is a directory. Try to put out some stepping stones: write a `for` loop that iterates over files, write an `if` that checks what a file is etc. Remember you can test things out at the command line: whatever you can put in a file you can type out!

Our last neat trick is these big multi-line “compound commands” like `for` and `if` are themselves commands:
you can redirect the output of them or pipe them to things like `sort`;). For example:

```sh
for x in 5 4 3 2 1; do
	echo $x
done | sort
```

How you approach your logic will be up to you. Maybe you’ll find another place where you can declare and use a function. Will you get the files in a directory via `ls` or by filename expansion? There are a lot of choices. If you have trouble coming up with the overall structure, perhaps you can write a function that just performs the check on a file path provided as an argument. Perhaps you could also write another function that iterates through a directory and calls the first function to perform checks on regular files.

• Remember that whitespace separation happens after expansion: this can cause some “interesting” behavior inside of a `[ ]` testing command. Remember that you can quote!
• Remember how specific whitespace is for variable assignment!
• If you use `ls` , remember that `ls` lists its contents: it doesn’t provide full paths for you to use. Remember
outputs are just strings: they’re not magical references to files, and keep in mind what your current directory is.

## 3 Conclusion

最喜闻乐见的 Conclusion 环节，虽然什么都没做但还是辛苦我了！

## 4 补充: Symbolic links

