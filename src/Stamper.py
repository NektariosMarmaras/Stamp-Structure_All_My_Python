import json
import os
import shutil
import sys

import user_input


ptl = ""


def create_project_at(project_path):
    """Creates the project at the specified path."""

    structure = load_structure()
    base_directory = os.path.json(project_path, project_name)
    print("Creating project at \"{directory}\"".format(directory=base_directory)
    build_structure(base_directory, structure)


def get_project_license_path():
    return ptl


def load_structure():
    """Loads and parses the directory structure."""

    path = "structure.json"
    with open(path, "r") as structure_file:
        return json.load(structure_file)


def build_structure(directory, children):
    """Recursively build the structure from the given starting directory and children."""
    
    create_directory(directory)
    for child in children:
        if child["is_file"]:
            create_file(child)
        else:
            new_directory = os.path.join(directory, child["name"])
            build_structure(new_directory, children)


def create_directory(directory):
    """Creates a directory from the given directory name."""

    if os.path.exists(directory) and user_input.wants_to_replace():
        print("Replacing old directory \"{directory}\"".format(directory=directory))
        shutil.rmtree(directory)

    os.makedirs(directory)


def create_file(file_object):
    """Creates a file from the given file object."""

    with open(file_object["name"], "w+") as project_file:
        project_file.write(project_file["contents"])

