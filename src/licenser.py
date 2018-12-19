import os
import mmap
import datetime

import user_input


class Licenser():
    def __init__(self):
        pass

    def choose_a_license(self, license_path):
        """Prompts the user to select a license."""

        self.licenses = self.get_available_licenses()
        print("\nAvailable licenses for immediate use:")
        for index, license in enumerate(self.licenses):
            print("{index}\t{license}".format(
                index=index,
                license=license,
            ))
        print(
            "\nIf you want to have a license not on that list, you can search for one at:\n"
            "https://opensource.org/licenses\n"
            "https://choosealicense.com\n"
        )

        self.license_prompt = (
            "Please select the desired license (0-{max}) or press 'c' to skip and add your own: ".format(
                max=len(self.licenses) - 1,
            )
        )
        self.choice = user_input.get_user_input(self.license_prompt)
        while self.choice not in ["c"] + ["C"] + [str(opt) for opt in range(len(self.licenses))]:
            print("Invalid input. Please try again.")
            self.choice = user_input.get_user_input(self.license_prompt)

        self.retVal = None
        if self.choice != "c" and self.choice != "C":
            self.copy_txt_from_selected_license(
                license_path, self.licenses[int(self.choice)])
            self.retVal = self.licenses[int(self.choice)]

        return self.retVal

    def get_available_licenses(self):
        """Searches for and returns a list of available licenses, sorted alphabetically."""

        return sorted([
            os.path.splitext(os.path.basename(license))[0] for license in os.listdir("data/licenses")
        ])

    def copy_txt_from_selected_license(self, license_path, license_name):
        """Copies the license template file, with user customization, to the project structure."""

        self.license_source_filename = "data/licenses/{license_name}.txt".format(
            license_name=license_name,
        )
        with open(self.license_source_filename, "r") as license_source_file:
            self.license_content = license_source_file.read()

        self.year_placeholder = "<YEAR>"
        self.copyright_placeholder = "<COPYRIGHT HOLDER>"
        if self.year_placeholder in self.license_content:
            self.license_content = self.license_content.replace(
                self.year_placeholder, str(datetime.datetime.now().year))
        if self.copyright_placeholder in self.license_content:
            self.copyright_holder = user_input.get_user_input(
                "What is your name or GitHub username? ")
            self.license_content = self.license_content.replace(
                self.copyright_placeholder, self.copyright_holder)

        with open(license_path, "w") as license_target_file:
            license_target_file.write(self.license_content)
