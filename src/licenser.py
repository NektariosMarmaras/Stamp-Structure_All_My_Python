import os
import mmap
import datetime

import stamper
import user_input


def choose_a_license(license_path):
    """Prompts the user to select a license."""

    licenses = get_available_licenses()
    print("\nAvailable licenses for immediate use:")
    for index, license in enumerate(licenses):
        print("{index}\t{license}".format(
            index=index,
            license=license,
        ))
    print(
        "\nIf you want to have a license not on that list, you can search for one at:\n"
        "https://opensource.org/licenses\n"
        "https://choosealicense.com\n"
    )

    license_prompt = (
        "Please select the desired license (0-{max}) or press 'c' to skip and add your own: ".format(
            max=len(licenses) - 1,
        )
    )
    choice = user_input.get_user_input(license_prompt)
    while choice not in ["c"] + [str(opt) for opt in range(len(licenses))]:
        print("Invalid input. Please try again.")
        choice = user_input.get_user_input(license_prompt)

    if choice != "c":
        copy_txt_from_selected_license(license_path, licenses[int(choice)])


def get_available_licenses():
    """Searches for and returns a list of available licenses, sorted alphabetically."""

    return sorted([
        os.path.splitext(os.path.basename(license))[0] for license in os.listdir("data/licenses")
    ])



def copy_txt_from_selected_license(license_path, license_name):
    """Copies the license template file, with user customization, to the project structure."""

    license_source_filename = "data/licenses/{license_name}.txt".format(
        license_name=license_name,
    )
    with open(license_source_filename, "r") as license_source_file:
        license_content = license_source_file.read()

    year_placeholder = "<YEAR>"
    copyright_placeholder = "<COPYRIGHT HOLDER>"
    if year_placeholder in license_content:
        license_content = license_content.replace(year_placeholder, str(datetime.datetime.now().year))
    if copyright_placeholder in license_content:
        copyright_holder = user_input.get_user_input("What is your name or GitHub username? ")
        license_content = license_content.replace(copyright_placeholder, copyright_holder)

    with open(license_path, "w") as license_target_file:
        license_target_file.write(license_content)
