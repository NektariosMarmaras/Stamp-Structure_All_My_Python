import os
import argparse

import licenser
import stamper


def setup_parser():
    """Prompts the user for input and builds the project structure."""

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path in which to build project structure")
    args = parser.parse_args()

    project_data = stamper.load_structure()
    structure = project_data["structure"]
    license_path = project_data["license_path"]

    project_path = stamper.create_project_at(args.path, structure)
    licenser.choose_a_license(os.path.join(project_path, license_path))


if __name__ == '__main__':
    setup_parser()
