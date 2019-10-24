r"""Example:
import haveFunWithFiles as hfwf
these = [(2, 'txt'), (3, 'html'), (4, 'css'), (5, 'py')]
for this in these:
    hfwf.createSomeDemoFiles(*this)
    
Hung Nguyen Thanh - hungnt89@gmail.com"""

import os
import sys


def createSomeDemoFiles(howMany=5, ext='txt'):
    """Create x files with extension y for demo!"""
    
    for i in range(howMany):
        with open(f"demoFile{i:0>2}.{ext}", "w") as f:
            print(f"Created demoFile{i:0>2}.{ext}")
            
    return None


def getFilesWithThisExt(ext='txt', includeSubfolders=False):
    """Return a list of files end in desired extension."""

    listFiles = []
    
    if includeSubfolders:
        for eachWalk in os.walk('.'):
            for filename in eachWalk[-1]:
                if filename.endswith(f".{ext}"):
                    listFiles.append(filename)
                else:
                    continue
    else:
        for filename in os.listdir():
            if filename.endswith(f".{ext}"):
                listFiles.append(filename)
                
    return listFiles


def delAllDemoFiles(includeSubfolders=False):
    """Delete all demo files. Let's start again."""

    def delFilesInCWD():
        for filename in os.listdir():
                if "demoFile" in filename:
                    os.remove(filename)
    
    def delAllFiles():
        for eachWalk in os.walk('.'):
            for filename in eachWalk[-1]:
                if 'demoFile' in filename:
                    filePath = os.path.join(eachWalk[0], filename)
                    os.remove(filePath)
                else:
                    continue

    print("-" * 50)
    print("You are about to delete all demoFile**!")
    print("Are you sure? 'Hell yeah'/'Mistake'")
    print("Or simply (y/n) if you want :)")
    
    while True:

        confirm = input("--> ")

        if confirm in ('y', 'Hell yeah'):
            if includeSubfolders:
                delAllFiles()
            else:
                delFilesInCWD()
            break
        elif confirm in ('n', 'Mistake'):
            print("Nothing happens. Don't worry!")
            break
        else:
            print("Non-sense! Use the given answers!")

    print("\nFiles DELETED!")

    return None


def createDemoTree():
    """Create a folder tree for test."""

    #TODO: Create random number of files with 3 random extensions.
    
    # Create Directories
    os.makedirs('TestFolder/Folder1/SubFolder1', exist_ok=True)
    os.makedirs('TestFolder/Folder1/SubFolder2', exist_ok=True)
    os.makedirs('TestFolder/Folder2/SubFolder1', exist_ok=True)
    os.makedirs('TestFolder/Folder2/SubFolder2', exist_ok=True)

    # Create Files
    def createDemoFiles(folder):
        with open(f"{folder.lower()}_file01.txt", "w"):
            pass
        with open(f"{folder.lower()}_file02.txt", "w"):
            pass
        return None

    os.chdir('TestFolder')
    createDemoFiles('TestFolder')
    os.chdir('Folder1')
    createDemoFiles('Folder1')
    os.chdir('SubFolder1')
    createDemoFiles('SubFolder1')
    os.chdir('../SubFolder2')
    createDemoFiles('SubFolder2')
    os.chdir('../../Folder2')
    createDemoFiles('Folder2')
    os.chdir('SubFolder1')
    createDemoFiles('SubFolder1')
    os.chdir('../SubFolder2')
    createDemoFiles('SubFolder2')

    print("\nTree created!\n")


if __name__ == '__main__':
    if sys.argv[1] == 'tree':
        createDemoTree()



# Author: Nguyen Thanh Hung
# Email: hungnt89@gmail.com
