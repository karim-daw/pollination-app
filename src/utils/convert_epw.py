import os
from ladybug.wea import Wea


def convertEPW(fileName: str) -> str:

    """ converts a epw file to a wea file and returns its file path """

    print("Converting epw file: {0}...".format(fileName))

    # build epw string
    filePathEpw = "src\weather-data\epw-files\\" + fileName

    # strip .epw from file name and put instead .wea
    strippedFileName = os.path.splitext(fileName)[0]
    newFileName  = strippedFileName + ".wea"
    filePathWea = "src\weather-data\wea-files\\" + newFileName

    try:
        # the actual conversion
        wea = Wea.from_epw_file(filePathEpw)
        wea_file = wea.write(filePathWea)

        print("Successfully converted epw file to a wea file...")
        return wea_file
    except:
        print("Something went wrong, check the name of the input file...")


