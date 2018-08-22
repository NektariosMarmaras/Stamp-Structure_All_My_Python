import os
import argparse
import Stamper
import licenser


path_to_license = ""


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("Path", type=str, help="The Desired Path")
    args = parser.parse_args()
    Stamper.create_project_at(args.Path)
    licenser.choose_a_license()


if __name__ == '__main__':
    setup_parser()
