"""
This script shows how to:

    1. create a room from a box
    2. add a single aperture to the south wall
    3. add the room to a model
    4. create a sensor grid and add it to the room
    5. save the room as an HBJSON file

"""

from genericpath import isdir
from honeybee.room import Room, Vector3D
from honeybee.model import Model
from honeybee_radiance.sensorgrid import SensorGrid
from ladybug_geometry.geometry3d.mesh import Mesh3D
from utils import folder_utils


class Shoebox:
    """ Shoebox class that creates a honeybee model based off a single room given a set of input parameters"""

    def __init__(self, width = 4.0, height = 3.5, depth = 6.0) -> None:
        # init dimensions
        self.width = width
        self.height = height
        self.depth = depth
        self._wwr = 0.5
        self._gridSize = 0.2
        self._gridOffset = 0.8
        self._room = Room
        self._model = Model
 
    # getters and setters for init dimensions
    @property
    def width(self) -> None:
        print("Getting width...{0}".format(self._width))
        return self._width
    
    @width.setter
    def width(self, value) -> None:
        print("Setting width...{0}".format(value))
        self._width = value

    @property
    def height(self) -> float:
        print("Getting width...{0}".format(self._height))
        return self._height
    
    @height.setter
    def height(self, value) -> None:
        print("Setting height...{0}".format(value))
        self._height = value

    @property
    def depth(self) -> float:
        print("Getting depth...{0}".format(self._depth))
        return self._depth
    
    @depth.setter
    def depth(self, value) -> None:
        print("Setting depth...{0}".format(value))
        self._depth = value

    # getters and setters for window to wall ratio
    @property
    def wwr(self) -> float:
        print("Getting wwr...{0}".format(self._wwr))
        return self._wwr

    @wwr.setter
    def wwr(self, value) -> None:
        print("Setting wwr...{0}".format(value))
        self._wwr = value
    
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

    # defining room
    def createRoom(self) -> None:
        """ creates a honeybee room based on width depth and height parameters"""

        print("Creating room...")
        # initiate a room
        room = Room.from_box(identifier='single_room', width=self.width, depth=self.depth, height=self.height)

        # get south facing wall
        # get south facing wall using wall face normal angle.
        south_vector = Vector3D(0, -1, 0)
        south_face = [face for face in room.faces if south_vector.angle(face.normal) <= 0.01][0]

        # create an aperture by ratio
        # alternatively one can use other methods like `aperture_by_width_height`
        # see here for docs: https://www.ladybug.tools/honeybee-core/docs/honeybee.face.html#honeybee.face.Face.aperture_by_width_height
        south_face.apertures_by_ratio(ratio=self.wwr)
        print("Successfully created room...{0}".format(room.identifier))

        self._room = room
    
    def createModel(self) -> None:
        """ creates a honeybee model based on a given honeybee room and a inputed sensor grid"""

        # create a model and add the room to it
        print("Creating model...")
        model: Model = Model('shoe-box', rooms=[self._room], units='Meters')

        # create a sensor grid - this is only required if you want to run grid-based studies
        # use generate_grid method to create a sensor grid from room floor
        grid_mesh: Mesh3D = self._room.generate_grid(x_dim=self.gridSize, y_dim=self.gridSize, offset=self.gridOffset)

        # create a sensor grid using the generated mesh and add to model
        sensor_grid: SensorGrid = SensorGrid.from_mesh3d(identifier='room', mesh=grid_mesh)
        model.properties.radiance.add_sensor_grid(sensor_grid)

        self._model: Model = model
        print("Successfully created model...{0}".format(self._model.identifier))
    
    def saveToHBJson(self) -> None:
        """ saves a .hbsjon file based off of a given honeybee model"""

        # check if folder exists, if not creat one
        print("Checking if output folder exists in root dir...")
        folderName: str = "honeybee-json-files"
        folder_utils.createFolder(folderName)

        # create file name
        width: float = "w" + str(self.width)
        height: float = "h" + str(self.height)
        depth: float = "d" + str(self.depth)
        wwr: float = "wrr" +  str(self.wwr)

        fileName: str = folder_utils.nameFile(width,height, depth, wwr)
        fileName = self._model.identifier + "_" + fileName

        self._model.to_hbjson(name=fileName, folder=folderName)
        print("Successfully saved model to .hbjson file...{0}".format(fileName))
    


