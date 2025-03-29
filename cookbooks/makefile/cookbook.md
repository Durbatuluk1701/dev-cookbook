# Makefile Cookbook

### General Information
Makefiles automate the build process for software projects. They define rules for compiling code, linking libraries, and running tests, making development more efficient.


### Installation
Make is typically installed by default on Unix/Linux systems. Windows users can use GNU Make via Cygwin or MinGW.


### Dependencies
Requires a POSIX-compliant shell environment.


### Build System
Make itself is the build system.


### Additional Resources
- GNU Make Manual: https://www.gnu.org/software/make/manual/make.html


---

## Table of Contents

- [Basic Build Rule](#basic-build-rule)
- [Phony Targets](#phony-targets)

## Recipes

### Basic Build Rule

Compile a C program from multiple object files.

```makefile
all: program

program: main.o utils.o
	gcc -o program main.o utils.o

main.o: main.c
	gcc -c main.c

utils.o: utils.c
	gcc -c utils.c

clean:
	rm -f *.o program

```
### Phony Targets

Define phony targets for running and cleaning.

```makefile
.PHONY: clean run

run: program
	./program

clean:
	rm -f *.o program

```
