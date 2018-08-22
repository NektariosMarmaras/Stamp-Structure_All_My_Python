import os
import shutil


ptl = ""


def create_project_at(project_path):
    folder_names = ["docs", "src", "test"]
    file_names = ["setup.py", "LICENSE.txt", "requirements.txt", "Makefile"]
    project_name = input("What is the name of the project? ")
    print(project_path + "\\" + project_name)
    create_folder(project_path, project_name, True)
    fin_proj_path = project_path + "\\" + project_name + "\\"
    i = 0
    while i < len(folder_names):
        create_folder(fin_proj_path, folder_names[i])
        i += 1
    i = 0
    while i < len(file_names):
        create_file(fin_proj_path, file_names[i])
        i += 1


def create_folder(dir_path, folder_name, is_project=False):
    des_dir = dir_path + "\\" + folder_name + "\\"
    try:
        if is_project:
            if not os.path.exists(des_dir):
                os.makedirs(des_dir)
            else:
                wtr = wants_to_replace()
                if wtr:
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
    test_to_write = None
    if file_name == "setup.py":
        test_to_write = "Package and distribution management."
    elif file_name == "sample.py":
        test_to_write = "The code of interest."
    elif file_name == "test_sample.py":
        test_to_write = "Package integration and unit tests."
    elif file_name == "requirements.txt":
        test_to_write = "Development dependencies."
    elif file_name == "LICENSE.txt":
        test_to_write = "Lawyering up."
    elif file_name == "Makefile.txt":
        test_to_write = "Generic management tasks."
    file_obj = open(fin_file_path, "w+")
    if test_to_write is not None:
        file_obj.write(test_to_write)
    file_obj.close()


def check_folder_name(folder_name):
    if folder_name == "docs":
        ret_val = None
    elif folder_name == "src":
        ret_val = "sample.py"
    elif folder_name == "test":
        ret_val = "test_sample.py"
    return ret_val


def wants_to_replace():
    ret_val = input("There is already a project with the same name.\n"
                   "Do you want to replace it?(y/n) ")
    while ret_val.lower() != "y" and ret_val.lower() != "n":
        print("Please Try Again")
        ret_val = input("Do you want to replace it?(y/n) ")
    if ret_val.lower() == "y":
        ret_val = True
    else:
        ret_val = False
    return ret_val


def get_project_license_path():
    return ptl
