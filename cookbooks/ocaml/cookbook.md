# OCaml Cookbook

### General Information
OCaml is a powerful, expressive functional language that also supports imperative and object-oriented programming. It is well-suited for rapid prototyping and production systems alike.


### Installation
Install OCaml via OPAM, the OCaml Package Manager. Follow the instructions at https://ocaml.org/docs/up-and-running.


### Dependencies
Use OPAM to manage libraries. Popular libraries include Core, Batteries, and Lwt for asynchronous programming.


### Build System
Dune is the recommended build system for OCaml. It simplifies project management, dependency resolution, and builds.


### Additional Resources
- Official site: https://ocaml.org
- Dune build system: https://dune.build
- OPAM package manager: https://opam.ocaml.org


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

Read a name from standard input and greet the user.

```ocaml
let () =
  print_string "Enter your name: ";
  let name = read_line () in
  Printf.printf "Hello, %s!\n" name

```
### Command Line Arguments

Iterate over command line arguments using Sys.argv.

```ocaml
let () =
  Array.iteri (fun i arg -> Printf.printf "Arg %d: %s\n" i arg) Sys.argv

```
### Recursive Factorial

Compute factorial recursively.

```ocaml
let rec factorial n =
  if n <= 1 then 1 else n * factorial (n - 1)
in
Printf.printf "Factorial of 5 is %d\n" (factorial 5)

```
### Regular Expression Usage

Use the Str module for regex matching.

```ocaml
#load "str.cma";;
let re = Str.regexp "[0-9]+" in
let test = "abc123def" in
if Str.string_match re test 0 then
  Printf.printf "Found number: %s\n" (Str.matched_string test)
else
  Printf.printf "No match found\n"

```
### String and List Functions

Manipulate strings and perform list operations.

```ocaml
let upper = String.uppercase_ascii "hello" in
let lst = [1; 2; 3; 4] in
let sum = List.fold_left (+) 0 lst in
Printf.printf "Uppercase: %s, Sum: %d\n" upper sum

```
### Module and Library Usage

Define a module and use its function.

```ocaml
module Math = struct
  let square x = x * x
end
let () =
  Printf.printf "Square of 3 is %d\n" (Math.square 3)

```
