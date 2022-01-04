from genericpath import isdir
from typing import List
from typing import Dict
from honeybee.room import Room, Vector3D
from honeybee.model import Model
from honeybee_radiance.sensorgrid import SensorGrid
from ladybug_geometry.geometry3d.mesh import Mesh3D
from utils import *

class FloorAnalysis:
    """ Floor analysis class that creates a honeybee model 
    based off of floor geometry"""

    def __init__(self, analysisName = "FloorAnalysis",analysisType = "AnnualDaylight" ) -> None:
        # init dimensions
        self.analysisName = analysisName
        self.analysisType = analysisType
        self._gridSize = 0.2
        self._gridOffset = 0.8
        self._room = Room
        self._model = Model

    def getParameterDict(self) -> Dict:
        """
        width: float = "w" + str(self.width)
        height: float = "h" + str(self.height)
        depth: float = "d" + str(self.depth)
        wwr: float = "wrr" +  str(self.wwr)
        """
        parameterDict = {
            "analysisName" : self.analysisName,
            "analysisType" : self.analysisType,
            "gridSize" : self.gridSize,
            "gridOffset" : self.gridOffset,
        }

        return parameterDict
    
    # getters and setters for analysis name and type
    @property
    def analysisName(self) -> None:
        print("Getting analysis name...{0}".format(self._analysisName))
        return self._analysisName
    
    @analysisName.setter
    def analysisName(self, value) -> None:
        print("Setting analysis name...{0}".format(value))
        self._analysisName = value

    @property
    def analysisType(self) -> None:
        print("Getting analysis name...{0}".format(self._analysisType))
        return self._analysisType
    
    @analysisType.setter
    def analysisType(self, value) -> None:
        print("Setting analysis type...{0}".format(value))
        self._analysisType = value

    # getters and setters for grid size
    @property
    def gridSize(self) -> float:
        print("Getting grid size...{0}".format(self._gridSize))
        return self._gridSize

    @gridSize.setter
    def gridSize(self, value) -> None:
        print("Setting grid size...{0}".format(value))
        self._gridSize = value

    # getters and setters for grid offset
    @property
    def gridOffset(self) -> float:
        print("Getting grid offset...{0}".format(self._gridOffset))
        return self._gridOffset

    @gridOffset.setter
    def gridOffset(self, value) -> None:
        print("Setting grid offset...{0}".format(value))
        self._gridOffset = value

    def createModel(self, sensor_grid: SensorGrid) -> None:
        """ creates a honeybee model based on a given honeybee room and a inputed sensor grid"""

        # create a model and add the room to it
        print("Creating model...")
        model: Model = Model('shoe-box', rooms=[self._room], units='Meters')

        # create a sensor grid using the generated mesh and add to model
        model.properties.radiance.add_sensor_grid(sensor_grid)

        self._model: Model = model
        print("Successfully created model...{0}".format(self._model.identifier))
        

    def saveToHBJson(hbModel: Model, projectFolder: str, projectName: str) -> None:
        """ saves a .hbsjon file based off of a given honeybee model"""

        # check if folder exists, if not creat one
        print("Checking if output folder exists in root dir...")
        folder_utils.createFolder(projectFolder)

        # create file name
        fileName = hbModel.identifier + "_" + projectName

        hbModel.to_hbjson(name=fileName, folder=projectFolder)
        print("Successfully saved model to .hbjson file...{0}".format(fileName))