import os
from typing import List

def createFolder(folderName: str) -> None:
    '''Check if directory exists, if not, create it'''
    
    myDir = folderName
    checkFolder = os.path.isdir(myDir)

    # If folder doesn't exist, then create it.
    if not checkFolder:
        os.makedirs(myDir)
        print("created folder : ", myDir)
    else:
        print(myDir, "folder already exists...")


def convertArgsToStrings(*args) -> str:
    """converts list of args to a concatenated string for file naming"""

    if args:
        fileName: str = ""
        for i, arg in enumerate(args):
            # convert to string
            arg = str(arg)
            #arg = str(arg)
            if i != len(args)-1:
                # add seperator
                arg += "_"
                fileName += arg
            else:
                fileName += arg
    else:
        fileName = "untitled.hbjson"
    
    return fileName

def convertKeyValueToString(dict,key) -> str:
    """ converts a single key value pair into a concatenated string"""
    if dict and key:
        # force cast key to string
        val = dict[key]
        valStr = str(val)
        keyStr = str(key)

        concantStr = keyStr + valStr
    else:
        concantStr = ""

    return concantStr





def total(xs: List[float]) -> float:
    result: float = 0.0
    for x in xs:
        result += x
    return result
    

