# find Cookbook

### General Information
Find is a versatile command-line tool used to search for files and directories based on criteria such as name, type, size, and modification time.


### Installation
Find is a standard utility on Unix/Linux systems.


### Dependencies
No external dependencies.


### Build System
Not applicable.


### Additional Resources
- GNU find manual: https://www.gnu.org/software/findutils/manual/html_mono/find.html


---

## Table of Contents

- [Find Files by Name](#find-files-by-name)
- [Find Directories](#find-directories)
- [Find Files by Modification Date](#find-files-by-modification-date)

## Recipes

### Find Files by Name

Search for files with a specific name.

```bash
find . -name "filename.txt"

```
### Find Directories

List all directories within the current directory.

```bash
find . -type d

```
### Find Files by Modification Date

Find files modified in the last 7 days.

```bash
find . -mtime -7

```
