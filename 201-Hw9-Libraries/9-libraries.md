# 9 Text Editor

## 9.1 Linking against libraries
In this section you’ll be linking against a static library and its dynamic version with two different targets.

1. `cd` into the link directory.
2. Run the `getlib.sh` script. This script identifies your operating system and architecture to locate and create links to the appropriate provided library files, putting down the `libthingy.so` and `libthingy.a` symlinks in the link directory.
3. Open the `Makefile` . Note the two TODOs.
4. As a foreword for Mac users, the `-l:libname.a`style of linking doesn’t work with the default tool chain on macOS. If you want to link a static library, you can simply provide the path to the static library file as an argument, just as if it were a source code file e.g. `gcc -o file1.c libname.a` .
5. Address the two TODOs and modify the compilation commands so that the `app-dynamic` target links against `libthingy.so` and the `app-static` target links against `libthingy.a` . When there’s a naming conflict, which takes precedence?
6. You can use the `run-dynamic` and `run-static` rules to see if you successfully linked against the dynamic and static libraries e.g. running $ `make run-dynamic` . For Linux/WSL users, try running `ldd` on your executables to see if they dynamically linked the libraries. For Mac users, you can use `otool -L` to provide similar information about your executables.

## 9.2 Creating libraries

In this section you’ll be performing the steps to build both a static library and a dynamic library.
1. `cd` into the create directory.
2. Take a look at the directory structure.
• The `inc` directory contains library header(s).
• The `libsrc` directory contains the source code for the library.
• The `lib` directory (created by the Makefile) contains produced libraries.
3. Open the `Makefile`. Note the four TODOs.
   1. Add the necessary commands to the appropriate recipes to build the object code for the dynamic and static libraries, the dynamic and static libraries themselves, and like in #1, update the `app-dynamic` and `app-static` targets to link against the appropriate libraries. For Mac users, remember that ` -l:libname.a` style linker arguments don’t work, and to provide the path to the static library as a normal file argument.
     • Note that dynamic/shared library objects need to be compiled as position-independent code.
     • Note that the object code has separate rules in the `Makefile`.