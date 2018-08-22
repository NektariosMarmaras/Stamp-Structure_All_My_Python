import os
import shutil
import sys


def get_user_input(message):
    # Support Python 2
    if sys.version_info >= (3, 0):
        return input(message)
    else:
        return raw_input(message)


ptl = ""


def create_project_at(project_path):
    folder_names = ["docs", "src", "test"]
    file_names = ["setup.py", "LICENSE.txt", "requirements.txt", "Makefile"]
    project_name = get_user_input("What is the name of the project? ")
    print(os.path.join(project_path, project_name))
    create_folder(project_path, project_name, True)
    fin_proj_path = os.path.join(project_path, project_name)
    for folder_name in folder_names:
        create_folder(fin_proj_path, folder_name)
    for file_name in file_names:
        create_file(fin_proj_path, file_name)


def create_folder(dir_path, folder_name, is_project=False):
    des_dir = os.path.join(dir_path, folder_name)
    try:
        if is_project:
            if not os.path.exists(des_dir):
                os.makedirs(des_dir)
            else:
                if wants_to_replace():
                    print("Replaced It!!")
                    shutil.rmtree(des_dir)
                    os.makedirs(des_dir)
                else:
                    print("Did Not Replace It!!")
        else:
            if not os.path.exists(des_dir):
                os.makedirs(des_dir)
            fold_name = check_folder_name(folder_name)
            if fold_name is not None:
                create_file(des_dir, fold_name)
    except OSError:
        print("OSError occured for given folder path " + des_dir)


def create_file(file_path, file_name):
    global ptl
    fin_file_path = os.path.join(file_path, file_name)
    if file_name == "LICENSE.txt":
        ptl = fin_file_path
    file_contents = {
        "setup.py": "Package and distribution management.",
        "sample.py": "The code of interest.",
        "test_sample.py": "Package integration and unit tests.",
        "requirements.txt": "Development dependencies.",
        "LICENSE.txt": "Lawyering up.",
        "Makefile": "Generic management tasks.",
    }
    with open(fin_file_path, "w+") as proj_file:
        proj_file.write(file_contents[file_name])


def check_folder_name(folder_name):
    if folder_name == "docs":
        ret_val = None
    elif folder_name == "src":
        ret_val = "sample.py"
    elif folder_name == "test":
        ret_val = "test_sample.py"
    return ret_val


def wants_to_replace():
    ret_val = get_user_input(
        "There is already a project with the same name.\n"
        "Do you want to replace it? (y/n) "
    )
    while ret_val.lower() not in ["y", "n"]:
        ret_val = get_user_input(
            "Please Try Again\n"
            "Do you want to replace it? (y/n) "
        )
    return ret_val.lower() == "y"


def get_project_license_path():
    return ptl
