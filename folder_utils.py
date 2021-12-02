
import os

# reference from https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/

def create_folder(folderName):
    '''Check if directory exists, if not, create it'''

    # You should change 'test' to your preferred folder.
    MYDIR = folderName
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)

    else:
        print(MYDIR, "folder already exists.")