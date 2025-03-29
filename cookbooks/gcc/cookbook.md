# gcc Cookbook

### General Information
GCC is the GNU Compiler Collection used for compiling C, C++, and other languages. It is highly configurable and supports multiple optimization and debugging options.


### Installation
Install GCC via your system package manager (e.g., apt, yum) or download it from https://gcc.gnu.org.


### Dependencies
Typically depends on system libraries. Additional libraries are specified via command-line flags.


### Build System
Often used with Makefiles or build systems like CMake.


### Additional Resources
- GCC Documentation: https://gcc.gnu.org/onlinedocs/


---

## Table of Contents

- [Compile a C Program](#compile-a-c-program)
- [Compile with Optimization](#compile-with-optimization)
- [Linking Multiple Files](#linking-multiple-files)

## Recipes

### Compile a C Program

Compile a simple C program with debugging symbols.

```bash
gcc -g -o program program.c

```
### Compile with Optimization

Compile a C program with optimization flags for improved performance.

```bash
gcc -O2 -o program program.c

```
### Linking Multiple Files

Compile and link multiple C source files into a single executable.

```bash
gcc -c file1.c
gcc -c file2.c
gcc -o program file1.o file2.o

```
