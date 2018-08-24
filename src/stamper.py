import json
import os
import shutil
import sys

import user_input


def create_project_at(project_path, structure):
    """Creates the project at the specified path."""

    project_name = user_input.get_user_input("What is the name of the project? ")
    base_directory = os.path.join(project_path, project_name)
    print("Creating project at \"{directory}\"".format(directory=base_directory))
    build_structure(base_directory, structure)

    return base_directory


def load_structure():
    """Loads and parses the directory structure."""

    with open("data/structure.json", "r") as structure_file:
        return json.load(structure_file)


def build_structure(directory, children):
    """Recursively build the structure from the given starting directory and children."""
    
    create_directory(directory)
    for child in children:
        if child["is_file"]:
            create_file(directory, child)
        else:
            new_directory = os.path.join(directory, child["name"])
            build_structure(new_directory, child["children"])


def create_directory(directory):
    """Creates a directory from the given directory name."""

    if os.path.exists(directory):
        if user_input.wants_to_replace():
            print("Replacing old directory \"{directory}\"".format(directory=directory))
            shutil.rmtree(directory)
        else:
            sys.exit()

    os.makedirs(directory)


def create_file(directory, file_object):
    """Creates a file from the given file object."""

    with open(os.path.join(directory, file_object["name"]), "w+") as project_file:
        project_file.write(file_object["contents"])

