import os
import json
import argparse

import user_input


class Config_Setup():
    def __init__(self):
        pass

    dat_set = {"name": "",
               "version": "",
               "license": ""}

    setup_pu_tmpl = """from distutils.core import setup

setup(
    name='{name}',
    version='{version}',
    packages={packages},
    license='{license}',
    long_description=open('{path_to_README}').read(),
    )"""

    def config(self, ptsf, proj_name, path_readme, lic_chosen=None):  # ptsf = Path To Setup_Data File
        '''Configure the setup file based on the data in the setup_data file'''
        self.dat_set["name"] = proj_name
        if lic_chosen != None:
            self.dat_set["license"] = lic_chosen

        self.edit_setup_data(self.dat_set, lic_chosen)
        with open(ptsf, "w") as f:
            f.write(self.setup_pu_tmpl.format(
                name=self.dat_set['name'], version=self.dat_set['version'], packages=self.packages_list, license=self.dat_set['license'], path_to_README=path_readme))

    def edit_setup_data(self, setup_dict, chosen_license):
        for item in setup_dict:
            if chosen_license == None and item == "license":
                continue
            self.item_msg = "Project's " + (item[:1].upper() + item[1:])
            if setup_dict[item] == "":
                self.msg_append = " : "
            else:
                self.msg_append = "[" + setup_dict[item] + "] : "
            self.item_msg = self.item_msg + self.msg_append
            self.ret_val = user_input.get_user_input(self.item_msg)
            if self.ret_val != "":
                setup_dict[item] = self.ret_val
            else:
                setup_dict[item] = setup_dict[item]

    def fill_list_of_packages(self, packageslist):
        self.packages_list = packageslist
