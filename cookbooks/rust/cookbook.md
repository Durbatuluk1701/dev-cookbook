# Rust Cookbook

### General Information
Rust is a modern systems programming language focused on safety, speed, and concurrency. Its strict compiler and powerful type system help prevent bugs at compile time.


### Installation
Install Rust via rustup from https://rustup.rs. Cargo, the build and package manager, comes bundled with the installation.


### Dependencies
Rust uses Cargo to manage dependencies. Popular crates include regex, serde, and tokio.


### Build System
Cargo serves as the build system, package manager, and test runner for Rust projects.


### Additional Resources
- Official site: https://www.rust-lang.org
- Cargo documentation: https://doc.rust-lang.org/cargo


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

Read input from the user and print a greeting.

```rust
use std::io;
fn main() {
    let mut input = String::new();
    println!("Enter your name:");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    println!("Hello, {}!", input.trim());
}

```
### Command Line Arguments

Iterate over command line arguments using std::env.

```rust
use std::env;
fn main() {
    for (i, arg) in env::args().enumerate() {
        println!("Arg {}: {}", i, arg);
    }
}

```
### Recursive Factorial

Define a recursive function to compute factorial.

```rust
fn factorial(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * factorial(n - 1) }
}
fn main() {
    println!("Factorial of 5 is {}", factorial(5));
}

```
### Regular Expression Usage

Use the regex crate to find a number in a string.

```rust
use regex::Regex;
fn main() {
    let re = Regex::new(r"\d+").unwrap();
    let text = "abc123def";
    if let Some(mat) = re.find(text) {
        println!("Found number: {}", mat.as_str());
    } else {
        println!("No match found");
    }
}

```
### String and List Functions

Convert a string to uppercase and sum the values of a vector.

```rust
fn main() {
    let upper = "hello".to_uppercase();
    let numbers = vec![1, 2, 3, 4];
    let sum: i32 = numbers.iter().sum();
    println!("Uppercase: {}, Sum: {}", upper, sum);
}

```
### Module and Library Usage

Define a module and call a function from it.

```rust
mod math {
    pub fn square(x: i32) -> i32 {
        x * x
    }
}
fn main() {
    println!("Square of 3 is {}", math::square(3));
}

```
