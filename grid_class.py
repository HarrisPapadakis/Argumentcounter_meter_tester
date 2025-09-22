def create_line_coordinates(cell_size: int) ->list[list[tuple]]:
    #Creates the x, y coordinates for drawing the grid lines

    points = []
    for y in range(1,9):
        #horizontal lines

        temp = []
        temp.append((0, y*cell_size)) #x,y points [(0,100), (0,200), (0,300) , (0,400)....]
        temp.append((900, y*cell_size)) #x,y points [(900,100), (900,200), (900,300) , (900,400)....]
        points.append(temp)

    for X in range(1,10):
        #Vertical lines -from 1 -10.to close the grid on the right side
        
        temp = []
        temp.append((x*cell_size,0)) #x,y points [(0,100), (0,200), (0,300) , (0,400)....]
        temp.append((x*cell_size,900)) #x,y points [(900,100), (900,200), (900,300) , (900,400)....]
        points.append(temp)


class Grid:
    def __init__(self):
        pass