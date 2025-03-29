# Bash Cookbook

### General Information
Bash is a Unix shell and scripting language used to automate tasks in Linux and Unix environments. It excels at text manipulation, command chaining, and process control.


### Installation
Bash is generally pre-installed on Linux and macOS. Windows users can use Git Bash or WSL.


### Dependencies
Bash relies on core Unix utilities. For extended functionality, GNU versions may be preferred.


### Build System
Bash scripts do not require a build system; however, Make can be used to orchestrate script execution.


### Additional Resources
- Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- Advanced Bash-Scripting Guide: https://tldp.org/LDP/abs/html/


---

## Table of Contents

- [Input/Output Example](#inputoutput-example)
- [Command Line Arguments](#command-line-arguments)
- [Recursive Factorial](#recursive-factorial)
- [Regular Expression Usage](#regular-expression-usage)
- [String and List Functions](#string-and-list-functions)
- [Module and Library Usage](#module-and-library-usage)

## Recipes

### Input/Output Example

Prompt the user for input and display a greeting.

```bash
#!/bin/bash
read -p "Enter your name: " name
echo "Hello, $name!"

```
### Command Line Arguments

Print the script name and all command line arguments.

```bash
#!/bin/bash
echo "Script name: $0"
for arg in "$@"; do
  echo "Argument: $arg"
done

```
### Recursive Factorial

Calculate factorial recursively using a Bash function.

```bash
#!/bin/bash
factorial() {
    if [ "$1" -le 1 ]; then
        echo 1
    else
        prev=$(factorial $(( $1 - 1 )))
        echo $(( $1 * prev ))
    fi
}
echo "Factorial of 5 is $(factorial 5)"

```
### Regular Expression Usage

Use grep to search for a numeric pattern in a string.

```bash
#!/bin/bash
text="abc123def"
if echo "$text" | grep -qE "[0-9]+"; then
    echo "Found a number in the text"
else
    echo "No number found"
fi

```
### String and List Functions

Convert a string to uppercase and sum elements of an array.

```bash
#!/bin/bash
text="hello"
upper=$(echo "$text" | tr '[:lower:]' '[:upper:]')
arr=(1 2 3 4)
sum=0
for i in "${arr[@]}"; do
    sum=$((sum + i))
done
echo "Uppercase: $upper, Sum: $sum"

```
### Module and Library Usage

Source another script to use its functions.

```bash
#!/bin/bash
# Assume utils.sh contains: function greet() { echo "Hello from utils!"; }
source ./utils.sh
greet

```
