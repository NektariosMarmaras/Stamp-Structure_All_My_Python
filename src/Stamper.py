import os
import argparse
import shutil


def SetupParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("Path", type=str, help="The Desired Path")
    args = parser.parse_args()
    createProjectAt(args.Path)


def createProjectAt(projectPath):
    folderNames = ["docs", "src", "test"]
    fileNames = ["setup.py", "LICENSE.txt", "requirements.txt", "Makefile.txt"]
    projectName = input("What is the name of the project? ")
    print(projectPath + "\\" + projectName)
    createFolder(projectPath, projectName, True)
    finProjPath = projectPath + "\\" + projectName + "\\"
    i = 0
    while i < 3:
        createFolder(finProjPath, folderNames[i])
        i += 1
    i = 0
    while i < 4:
        createFile(finProjPath, fileNames[i])
        i += 1


def createFolder(dirPath, folderName, isProject=False):
    desDir = dirPath + "\\" + folderName + "\\"
    try:
        if isProject:
            if not os.path.exists(desDir):
                os.makedirs(desDir)
            else:
                wTr = wantsToReplace()
                if wTr:
                    print("Replaced It!!")
                    shutil.rmtree(desDir)
                    os.makedirs(desDir)
                else:
                    print("Did Not Replace It!!")
        else:
            if not os.path.exists(desDir):
                os.makedirs(desDir)
            foldName = checkFolderName(folderName)
            if foldName is not None:
                createFile(desDir, foldName)
    except OSError:
        print("OSError occured for given folder path " + desDir)


def createFile(filePath, fileName):
    finFilePath = os.path.join(filePath, fileName)
    textToWrite = None
    if fileName == "setup.py":
        textToWrite = "Package and distribution management."
    elif fileName == "sample.py":
        textToWrite = "The code of interest."
    elif fileName == "test_sample.py":
        textToWrite = "Package integration and unit tests."
    elif fileName == "requirements.txt":
        textToWrite = "Development dependencies."
    elif fileName == "LICENSE.txt":
        textToWrite = "Lawyering up."
    elif fileName == "Makefile.txt":
        textToWrite = "Generic management tasks."
    fileOBJ = open(finFilePath, "w+")
    if textToWrite is not None:
        fileOBJ.write(textToWrite)
    fileOBJ.close()


def checkFolderName(folderName):
    if(folderName == "docs"):
        retVal = None
    elif(folderName == "src"):
        retVal = "sample.py"
    elif(folderName == "test"):
        retVal = "test_sample.py"
    return retVal


def wantsToReplace():
    retVal = input("There is already a project with the same name.\n"
                   "Do you want to replace it?(y/n) ")
    while (retVal.lower() != "y" and retVal.lower() != "n"):
        print("Please Try Again")
        retVal = input("Do you want to replace it?(y/n) ")
    if retVal.lower() == "y":
        retVal = True
    else:
        retVal = False
    return retVal


if(__name__ == '__main__'):
    SetupParser()
