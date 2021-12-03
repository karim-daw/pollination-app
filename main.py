import shoe_box





# init shoe_box 
sb = shoe_box.Shoebox(width=6.0 , height=4.0 , depth=10.0 )

sb.gridSize = 0.5
sb.gridOffset = 0.75
sb.wwr = 0.4

# create room
room = sb.createRoom()

# run
if __name__ == "__main__":
    # create model
    sb.createModel()
