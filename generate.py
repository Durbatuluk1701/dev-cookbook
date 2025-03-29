#!/usr/bin/env python3
import yaml
import os
from jinja2 import Environment, FileSystemLoader, Template
import sys
import re
import argparse

TEMPLATE_FOLDER = "_templates"
COOKBOOK_TEMPLATE = f"{TEMPLATE_FOLDER}/cookbook.md.jinja"
README_TEMPLATE = f"{TEMPLATE_FOLDER}/readme.md.jinja"
TOP_LEVEL_DIRS = ["cookbooks"]

type JinjaDict = dict[str, dict[str, str]]


def regex_replace(s, find, replace):
    return re.sub(find, replace, s)


def markdown_safe_link(s: str) -> str:
    s = s.lower().replace(" ", "-")
    s = re.sub("[^a-z\\-]", "", s)
    s = re.sub("-+", "-", s)
    return s


def load_jinja_template(template_file: str) -> Template:
    # Set up jinja2
    env = Environment(
        loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True
    )
    env.filters["regex_replace"] = regex_replace
    env.filters["markdown_safe_link"] = markdown_safe_link

    # Load the Jinja template
    try:
        template = env.get_template(template_file)
    except Exception as e:
        sys.exit(f"Error loading template: {e}")

    return template


def generate_cookbook(yaml_file: str) -> tuple[str, str]:
    # open yaml file
    try:
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        sys.exit("Error: data.yaml file not found.")

    template = load_jinja_template(COOKBOOK_TEMPLATE)

    # Render the template with data from the YAML file
    output = template.render(data)

    # Write the rendered output to a markdown file
    output_dir = os.path.dirname(yaml_file)
    yaml_file_name = os.path.splitext(os.path.basename(yaml_file))[0]
    out_file = f"{output_dir}/cookbook.md"
    print(f"Writing to {out_file}...")
    with open(out_file, "w") as f:
        f.write(output)

    return (yaml_file_name, out_file)


def generate_readme(cookbooks: JinjaDict) -> None:
    template = load_jinja_template(README_TEMPLATE)

    # Render the template with data from the YAML file
    output = template.render(cookbooks)

    # Write the rendered output to a markdown file
    with open("README.md", "w") as f:
        f.write(output)


def find_all_files():
    for dir in TOP_LEVEL_DIRS:
        for root, _, files in os.walk(dir):
            for file in files:
                yield os.path.join(root, file)


def clean():
    for file in find_all_files():
        if file.endswith(".md"):
            print(f"Removing {file}...")
            os.remove(file)


def build_cookbooks() -> JinjaDict:
    # find all the yaml files in "cookbooks" directory
    cookbooks = {}
    for file in find_all_files():
        if file.endswith(".yaml"):
            print(f"Generating cookbook from {file}...")
            lang, cookbook = generate_cookbook(file)
            cookbooks[lang] = cookbook
    return {"cookbooks": cookbooks}


def build_top_readme(cookbooks: JinjaDict) -> None:
    generate_readme(cookbooks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a cookbook markdown file from a YAML file."
    )
    parser.add_argument(
        "--mode",
        choices=["build", "clean"],
        default="build",
        help="Mode to run the script in.",
    )
    args = parser.parse_args()
    match args.mode:
        case "build":
            build_top_readme(build_cookbooks())
        case "clean":
            clean()
        case _:
            sys.exit("Error: Invalid mode. Use 'build' or 'clean'.")
