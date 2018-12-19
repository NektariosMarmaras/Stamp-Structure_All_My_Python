import json
import os
import shutil
import sys

import user_input


class Stamper():
    def __init__(self, packageslist=None):
        self.packages_list = packageslist

    def create_project_at(self, project_path, structure):
        """Creates the project at the specified path."""

        self.project_name = user_input.get_user_input(
            "What is the name of the project? ")
        self.base_directory = os.path.join(project_path, self.project_name)
        print("Creating project at \"{directory}\"".format(
            directory=self.base_directory))
        self.build_structure(self.base_directory, structure)

        return {"path": self.base_directory, "name": self.project_name}

    def load_structure(self):
        """Loads and parses the directory structure."""

        with open("data/structure.json", "r") as structure_file:
            return json.load(structure_file)

    def build_structure(self, directory, children):
        """Recursively build the structure from the given starting directory and children."""
        self.create_directory(directory)
        for child in children:
            if child["is_file"]:
                self.create_file(directory, child)
            else:
                self.new_directory = os.path.join(directory, child["name"])
                if child["is_package"]:
                    self.packages_list.append(child["name"])
                self.build_structure(self.new_directory, child["children"])

    def create_directory(self, directory):
        """Creates a directory from the given directory name."""

        if os.path.exists(directory):
            if user_input.wants_to_replace():
                print("Replacing old directory \"{directory}\"".format(
                    directory=directory))
                shutil.rmtree(directory)
            else:
                sys.exit()

        os.makedirs(directory)

    def create_file(self, directory, file_object):
        """Creates a file from the given file object."""

        with open(os.path.join(directory, file_object["name"]), "w+") as project_file:
            project_file.write(file_object["contents"])
