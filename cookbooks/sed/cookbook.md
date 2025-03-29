# Sed Cookbook

### General Information
Sed is a stream editor used for filtering and transforming text in a pipeline. It is highly efficient for batch editing files or streams.


### Installation
Sed is usually pre-installed on Unix/Linux systems. GNU sed is recommended for its extended features.


### Dependencies
No external dependencies are needed.


### Build System
Not applicable – Sed scripts run directly in the shell.


### Additional Resources
- GNU sed manual: https://www.gnu.org/software/sed/manual/sed.html


---

## Table of Contents

- [Basic Substitution](#basic-substitution)
- [Delete Lines Matching Pattern](#delete-lines-matching-pattern)
- [In-place Editing](#in-place-editing)

## Recipes

### Basic Substitution

Replace all occurrences of 'foo' with 'bar' in a file.

```bash
sed 's/foo/bar/g' input.txt > output.txt

```
### Delete Lines Matching Pattern

Delete lines that match a given pattern.

```bash
sed '/pattern/d' input.txt

```
### In-place Editing

Replace 'hello' with 'world' in the file without creating a new file.

```bash
sed -i 's/hello/world/g' file.txt

```
