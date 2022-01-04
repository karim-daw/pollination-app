from utils import *
from honeybee.model import Model


def saveToHBJson(hbModel: Model, projectFolder: str, projectName: str) -> None:
    """ saves a .hbsjon file based off of a given honeybee model"""

    # check if folder exists, if not creat one
    print("Checking if output folder exists in root dir...")
    folder_utils.createFolder(projectFolder)

    # create file name
    fileName = hbModel.identifier + "_" + projectName

    hbModel.to_hbjson(name=fileName, folder=projectFolder)
    print("Successfully saved model to .hbjson file...{0}".format(fileName))