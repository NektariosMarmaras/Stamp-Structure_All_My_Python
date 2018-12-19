import argparse
import os

from licenser import Licenser
from setup_config import Config_Setup
from stamper import Stamper


class main_stamp():
    def __init__(self):
        self.list_of_packages = []
        self.lic_nse = Licenser()
        self.sta_per = Stamper(self.list_of_packages)
        self.con_set = Config_Setup()
        self.con_set.fill_list_of_packages(self.list_of_packages)
        self.setup_parser()

    def setup_parser(self):
        """Prompts the user for input and builds the project structure."""

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "path", type=str, help="Path in which to build project structure")
        self.args = self.parser.parse_args()

        self.project_structure = self.sta_per.load_structure()
        self.structure = self.project_structure["structure"]
        self.license_file = self.project_structure["license_path"]
        self.readme_file = self.project_structure["readme_path"]
        self.spp = self.project_structure["setup_py_path"]  # Setup_Py_Path

        self.project_info = self.sta_per.create_project_at(
            self.args.path, self.structure)

        self.path_to_setup_py = os.path.join(
            self.project_info["path"], self.spp)

        self.con_set.config(self.path_to_setup_py,
                            self.project_info["name"], self.readme_file)

        self.lic_chosen = None
        self.lic_chosen = self.lic_nse.choose_a_license(
            os.path.join(self.project_info["path"], self.license_file))
        print(self.lic_chosen)
        self.con_set.config(self.path_to_setup_py,
                            self.project_info["name"], self.readme_file, self.lic_chosen)

    def get_packages(self):
        return self.list_of_packages


if __name__ == '__main__':
    main_stamp()
