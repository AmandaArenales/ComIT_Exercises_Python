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

    def __init__(self, *args):
        if (len(args) == 2):
            self.position_x = args[0]
            self.position_y = args[1]
    
    def set_setXY(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        print(f"The position of the coordinate (x, y) is: ({position_x, position_y})")

    def get_position_x_y(self):
        return (self.position_x, self.position_y)
    
    def increase_value(self, incX, incY):
        incX = self.position_x + incX
        incY = self.position_y + incY
        print(f"The value of the new the coordinate (x, y) after increment it is: ({incX, incY})")

    def decrease_value(self, decX, decY):
        decX = self.position_x - decX
        decY = self.position_y - decY
        print(f"The value of the new the coordinate (x, y) after decrement it is: ({decX, decY})")

x = int(input("P1 - insert the value for x: "))
y = int(input("P1 - insert the value for y: "))

p1 = Position()
p1.set_setXY(x, y)

inc_x =  int(input("Please, insert the increasing value for the position x: "))
inc_y =  int(input("Please, insert the increasing value for the position y: "))

p1.increase_value(inc_x, inc_y)

dec_x =  int(input("Please, insert the decreasing value for the position x: "))
dec_y =  int(input("Please, insert the decreasing value for the position y: "))

p1.decrease_value(dec_x, dec_y)

x = int(input("P2 - insert the value for x: "))
y = int(input("P2 - insert the value for y: "))

p2 = Position(x, y)

inc_x =  int(input("Please, insert the increasing value for the position x: "))
inc_y =  int(input("Please, insert the increasing value for the position y: "))

p2.increase_value(inc_x, inc_y)

dec_x =  int(input("Please, insert the decreasing value for the position x: "))
dec_y =  int(input("Please, insert the decreasing value for the position y: "))

p2.decrease_value(dec_x, dec_y)