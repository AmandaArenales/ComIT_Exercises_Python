"""Implement the class Position that represents a coordinate (x, y). Each position is defined 
by two integer values ​​x and y. Available operations are:

· Default constructor, corresponds to the position (0,0). 
· Constructor with initial values ​​of X and Y 
· Methods for modifying and querying (set / get) the attributes of the class. 
· Methods for increasing and decreasing the values ​​of each of the position coordinates (incX, incY, decX, decY). 
· A method for setting coordinate values ​​(setXY)."""

class Position:
    position_x= 0
    position_y = 0
    incX = 0
    incY = 0
    decX = 0
    decY = 0

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif (len(args) == 2):
            self.position_x = args[0]
            self.position_y = args[1]
        elif (len(args) == 4):
            self.position_x = args[0]
            self.position_y = args[1]
    
    def set_setXY(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        print(f"The position of the coordinate (x, y) is: ({position_x, position_y})")

    def get_position_x_y(self, position_x, position_y):
        return (position_x, position_y)
    
    def increase_value(self, incX, incY):
        incX = self.position_x + incX
        incY = self.position_y + incY
        print(f"The value of the new the coordinate (x, y) after increment it is: ({incX, incY})")

    def decrease_value(self, decX, decY):
        decX = self.position_x - decX
        decY = self.position_y - decY
        print(f"The value of the new the coordinate (x, y) after decrement it is: ({decX, decY})")

x = int(input("Please, insert the value for the position x: "))
y = int(input("Please, insert the value for the position y: "))

p = Position()
p.set_setXY(x, y)

inc_x =  int(input("Please, insert the increasing value for the position x: "))
inc_y =  int(input("Please, insert the increasing value for the position y: "))

p.increase_value(inc_x, inc_y)

dec_x =  int(input("Please, insert the decreasing value for the position x: "))
dec_y =  int(input("Please, insert the decreasing value for the position y: "))

p.decrease_value(dec_x, dec_y)
