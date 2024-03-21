# 7-make-basic

## 7.1 Start

1. `cd` into `1`  directory.
2. Create a file named `Makefile`.
3. Create a rule with a target called all that has this for a recipe: `gcc -o nocat nocat.c`
4. Create a rule with target called `clean` that has this for a recipe: `rm -f nocat`
5. Move the `all` rule to the top so that it’ll run by default when `make` is run without a target specified.
6. Make sure that your Makefile works correctly.
7.  Add and commit `Makefile` .

## 7.2 Phonies

1. `cd` into `2` directory
2. Take a look at `Makefile`, try running `make all` , `make clean` , and `make test` . Note that their recipes do not run. Fix the `Makefile` so that each of the rules can run their recipes

```c++
.PHONY: all
all:
	echo "This is the 'all' target"

.PHONY: clean
clean:
	echo "This is the 'clean' target"

.PHONY: test
test:
	echo "This is the 'test' target"

```

## 7.3 Dependencies

1. `cd` into the `3` directory.
2. Take a look at the Makefile. Note what each target in the Makefile requires which file.
3. Edit the Makefile so that each target has the proper prerequisites. One way to test this is to run to delete any (one or all) intermediate build files, and then run `make <some target>` (e.g. `make nocat`) to build one of the targets. The build should succeed as Make will proceed to build any missing intermediate files, and the only files that should be built are the ones that are missing.
4. Another test you can do is to `touch` one of the source code files and or its intermediate outputs, then to run Make. Updating a file’s timestamp via `touch` will cause Make to see it as a file that was updated more recently and thus require a rebuild of files that depend on it: this can point out issues in the dependency chain you represent in the prerequisites of rules.
5. The code does compile. Ignore any warnings that the compiler prints out: these are just warnings and are not errors.

## 7.4 Not repeating yourself

Create the `Makefile` so that:

• It has a `CC` variable that is set to `gcc`. This variable represents which C compiler to use.

• It has a `BIN` variable that is set to `sum30`. This variable represents what the output executable binary is named.

• It has a `SRCS` variable that contains all the `.c` files under the `src` directory. This list should not be hardcoded (for this assignment): if a new `.c` file is added, the Makefile should not have to be edited to include it.

• It has a rule to build the output executable binary. Don’t worry about object code. Note that the`-o` flag for `gcc` sets the output name. This rule should have `SRCS` as a prerequisite. In addition, the recipe should make use of existing variables and automatic variables that refer to the target and prerequisites to avoid repeating yourself (e.g. you shouldn’t be referring to `SRCS` or `BIN` in the compilation command).

• There is a phony `all` target that builds the output executable binary.

• There is a phony `clean` target that removes the output executable binary.

• The `all` target should run when `make` is run (without a target specified).