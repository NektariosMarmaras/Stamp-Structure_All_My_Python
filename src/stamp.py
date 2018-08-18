import os
import argparse
import Stamper


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("Path", type=str, help="The Desired Path")
    args = parser.parse_args()
    Stamper.create_project_at(args.Path)


if __name__ == '__main__':
    setup_parser()
