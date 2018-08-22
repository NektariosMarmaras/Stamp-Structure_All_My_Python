import os
import mmap
import datetime
import Stamper


def choose_a_license():
    fsl = find_selected_license()
    print("\nAvailable licenses for immediate use: ")
    for index, lic_item in enumerate(fsl):
        print(str(index) + ") " + str(lic_item))
    lic_index = input("\nIf you want to have a license other than those we have you can search for one at :\n"
                      "1) https://opensource.org/licenses\n"
                      "2) https://choosealicense.com/\n"
                      "\nPlease select the desirable license[0-" + str((len(fsl)-1)) + "] or\n"
                      "press 'c' if you want to add another license. ")
    if lic_index is not 'c':
        file_lines = []
        selected_license = fsl[int(lic_index)]
        licence_name = find_selected_license(selected_license)
        copy_txt_from_selected_license(licence_name)


def find_selected_license(sel_lic_name = None):
    lic_names = []
    for diname, subdirnames, filenames in os.walk('LICENSES'):
        for file_name in filenames:
            lic_name = os.path.splitext(file_name)[0]
            if sel_lic_name is None:
                lic_names.append(lic_name)
            else:
                if lic_name == sel_lic_name:
                    print('lic_name ' +lic_name)
                    return lic_name
    return lic_names


def copy_txt_from_selected_license(lic_name):
    year_str = '<YEAR>'
    copyright_holder_str = '<COPYRIGHT HOLDER>'
    tlf = Stamper.get_project_license_path()
    now = datetime.datetime.now()
    with open("./LICENSES/" + lic_name + ".txt", "r") as source_license_file:
        with open(tlf, "w") as target_license_file:
            for line in source_license_file:
                if year_str in line:
                    line = line.replace(year_str, str(now.year))
                if copyright_holder_str in line:
                    holder_name = input("What's your github username? ")
                    line = line.replace(copyright_holder_str, holder_name)
                target_license_file.write(line)
