#Given the radius of a circle, make an algorithm to calculate the value of the area.

from math import pi

def circle_area():
    r = float(input("Please, insert the radius of a circle: "))
    area = pi * r ** 2
    print (f"Given the radius equal {r}, the circle area is: {area}")
	
circle_area()
