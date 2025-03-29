# AWK Cookbook

### General Information
AWK is a domain-specific language designed for text processing and data extraction. It excels at scanning and transforming text files, especially for reporting tasks.


### Installation
AWK is typically pre-installed on Unix/Linux systems. GNU Awk (gawk) is recommended for additional features.


### Dependencies
No external dependencies are required.


### Build System
Not applicable.


### Additional Resources
- GNU Awk Manual: https://www.gnu.org/software/gawk/manual/gawk.html


---

## Table of Contents

- [Basic AWK Print](#basic-awk-print)
- [Pattern Matching](#pattern-matching)
- [Field Separator](#field-separator)

## Recipes

### Basic AWK Print

Print the first field of each line in a file.

```bash
awk '{print $1}' input.txt

```
### Pattern Matching

Print lines where the second field is greater than 100.

```bash
awk '$2 > 100 {print}' input.txt

```
### Field Separator

Process a CSV file using a comma as the field separator.

```bash
awk -F"," '{print $1, $2}' input.csv

```
