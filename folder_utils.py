import os

def create_folder(folderName) -> None:
    '''Check if directory exists, if not, create it'''
    
    # reference from https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/

    # You should change 'test' to your preferred folder.
    myDir = folderName
    checkFolder = os.path.isdir(myDir)

    # If folder doesn't exist, then create it.
    if not checkFolder:
        os.makedirs(myDir)
        print("created folder : ", myDir)

    else:
        print(myDir, "folder already exists...")


def name_file(*args):
    """converts list of args to a string for file nameing"""

    if args:
        fileName = ""
        for i, arg in enumerate(args):
            # convert to string
            arg = str(arg)
            if i != len(args)-1:
                # add seperator
                arg += "_"
                fileName += arg
            else:
                fileName += arg
    else:
        fileName = "Untitled.hbjson"
    
    return fileName
