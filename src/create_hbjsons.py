from models import shoe_box

def createHBjsons() -> None:
    
    for i in range(4):
        
        # increment on shoebox dimensions
        _width = 4.0 + i*0.5
        _height = 3.5 + i*0.1
        _depth = 4.0 + i*0.5

        # init shoe_box 
        sb = shoe_box.Shoebox(width=_width , height=_height , depth=_depth )

        # set grid size and offset
        sb.gridSize = 0.5
        sb.gridOffset = 0.75

        # set window to wall ratio
        sb.wwr = 0.4

        # create room
        sb.createRoom()

        # create model
        sb.createModel()

        # save to hbjson
        sb.saveToHBJson()

# run
if __name__ == "__main__":

    # create models
    createHBjsons()
