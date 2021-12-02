import os

def create_folder(folderName):
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
        print(myDir, "folder already exists.")