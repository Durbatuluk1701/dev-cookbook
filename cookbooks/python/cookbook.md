# Python Cookbook

### General Information
Python is a versatile, high-level language known for its readability and extensive standard library. It is widely used for web development, data analysis, automation, and more.


### Installation
Download Python from https://python.org and install via the official installer. Use pip to manage additional packages. On Ubuntu 24.04, Python is usually pre-installed; you may need to install the venv module using:

    sudo apt update
    sudo apt install python3-venv


### Dependencies
Python’s rich ecosystem includes packages like requests, numpy, and pandas. The standard library is also very comprehensive.


### Build System
Python projects are commonly managed with setuptools, pip, or poetry for packaging and dependency management.


### Additional Resources
- Official site: https://python.org
- PyPI: https://pypi.org


---

## Table of Contents

- [Input/Output Example](#inputoutput-example)
- [Command Line Arguments](#command-line-arguments)
- [Command Line Arguments (argparse)](#command-line-arguments-argparse)
- [Recursive Factorial](#recursive-factorial)
- [Regular Expression Usage](#regular-expression-usage)
- [String and List Functions](#string-and-list-functions)
- [Module and Library Usage](#module-and-library-usage)
- [Virtual Environment Setup](#virtual-environment-setup)

## Recipes

### Input/Output Example

Prompt for input and print a greeting.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")

```
### Command Line Arguments

Access command line arguments using sys.argv.

```python
import sys
for i, arg in enumerate(sys.argv):
    print(f"Arg {i}: {arg}")

```
### Command Line Arguments (argparse)

Utilize the argparse library for advanced command line argument parsing.

```python
import argparse
parser = argparse.ArgumentParser(description="Description of executable.")
parser.add_argument("name", type=str, help="A string argument for variable 'name' based on position.")
parser.add_argument("--testarg", type=int, help="An integer argument parsable via '--testarg <int>' and accessible via 'args.testarg'.")
parser.add_argument('--mode', choices=['train', 'test'], help='A finite set of choices for the mode argument.')

```
### Recursive Factorial

Calculate factorial recursively.

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
print("Factorial of 5 is", factorial(5))

```
### Regular Expression Usage

Use the re module to extract a number from a string.

```python
import re
text = "abc123def"
match = re.search(r"\d+", text)
if match:
    print("Found number:", match.group())
else:
    print("No match found")

```
### String and List Functions

Manipulate strings and operate on lists.

```python
upper = "hello".upper()
numbers = [1, 2, 3, 4]
total = sum(numbers)
print(f"Uppercase: {upper}, Sum: {total}")

```
### Module and Library Usage

Import a module and use its functionality.

```python
import math
print("Square root of 16 is", math.sqrt(16))

```
### Virtual Environment Setup

Set up a Python virtual environment on Ubuntu 24.04 using the built-in venv module.

```bash
# Update package lists and install python3-venv if not already installed
sudo apt update
sudo apt install python3-venv

# Create a virtual environment in the 'venv_dir' directory
python3 -m venv venv_dir

# Activate the virtual environment
source venv_dir/bin/activate

# Upgrade pip and install any required packages
pip install --upgrade pip

```
