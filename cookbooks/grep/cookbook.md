# grep Cookbook

### General Information
Grep is a command-line utility that searches for patterns within text. It is optimized for speed and supports regular expressions for advanced searching.


### Installation
Grep is typically pre-installed on Unix/Linux systems. GNU grep is commonly used.


### Dependencies
No external dependencies.


### Build System
Not applicable.


### Additional Resources
- GNU grep manual: https://www.gnu.org/software/grep/manual/grep.html


---

## Table of Contents

- [Basic Search](#basic-search)
- [Recursive Search](#recursive-search)
- [Case-insensitive Search](#case-insensitive-search)

## Recipes

### Basic Search

Search for a specific pattern in a file.

```bash
grep "pattern" file.txt

```
### Recursive Search

Search for a pattern recursively in a directory.

```bash
grep -r "pattern" /path/to/directory

```
### Case-insensitive Search

Perform a case-insensitive search for a pattern.

```bash
grep -i "pattern" file.txt

```
