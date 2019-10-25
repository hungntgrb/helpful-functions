r"""Example:
import haveFunWithFiles as hfwf
these = [(2, 'txt'), (3, 'html'), (4, 'css'), (5, 'py')]
for this in these:
    hfwf.createSomeDemoFiles(*this)

>>> python haveFunWithFiles.py -tree  =>  create a dummy tree!
    
Hung Nguyen Thanh - hungnt89@gmail.com"""

import os
import sys
import random

def createSomeRandomDemoFiles(howMany=5, folder=None):
    """Create x files with random extension for playing around!"""

    exts = ['txt','docx','xlsx','csv','json','py','js','xml','yaml','html','css','mp3','mp4']
    
    if folder:
        fn = f"{folder}_demoFile"
    else:
        fn = "demoFile"
    
    for i in range(howMany):
        ext = random.choice(exts)
        with open(f"{fn}{i:0>2}.{ext}", "wb") as f:
            print(f"Created {fn}{i:0>2}.{ext}")

    print('DONE! Perfect.')
            
    return None


def createSomeDemoFiles(howMany=5, ext='txt'):
    """Create x files with extension y for demo!"""
    
    for i in range(howMany):
        with open(f"demoFile{i:0>2}.{ext}", "w") as f:
            print(f"Created demoFile{i:0>2}.{ext}")
            
    print('DONE! Perfect.')
            
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
    """Delete all demoFiles. Let's start again."""

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
    print("You are about to delete all demoFiles!")
    print("Are you sure? 'Hell yeah'/'Mistake'")
    print("Or simply y/n if you want :)")
    
    while True:

        confirm = input("--> ")

        if confirm in ('y', 'Hell yeah'):
            if includeSubfolders:
                delAllFiles()
            else:
                delFilesInCWD()
                
            print("\nFiles DELETED!")
            break
        
        elif confirm in ('n', 'Mistake'):
            print("Nothing happens. Don't worry!")
            break
        
        else:
            print("Non-sense! Use the given answers!")

    return None


def createDemoTree():
    """Create a folder tree for playing around."""
    
    # Create Directories
    os.makedirs('testFolder/f1/f1s', exist_ok=True)
    os.makedirs('testFolder/f2/f2s', exist_ok=True)
    
    # Create Files

    os.chdir('testFolder')
    createSomeRandomDemoFiles(howMany=10)
    os.chdir('f1')
    createSomeRandomDemoFiles(howMany=10, folder='f1')
    os.chdir('f1s')
    createSomeRandomDemoFiles(howMany=10, folder='f1s')
    os.chdir('../../f2')
    createSomeRandomDemoFiles(howMany=10, folder='f2')
    os.chdir('f2s')
    createSomeRandomDemoFiles(howMany=10, folder='f2s')
   

    print("\nTree CREATED!\n")


if __name__ == '__main__':
    if sys.argv[1] == '-tree':
        createDemoTree()



# Author: Nguyen Thanh Hung
# Email: hungnt89@gmail.com
