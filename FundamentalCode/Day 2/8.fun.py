pi=3.14
def areaOfCircle(radius):
    return 2*pi*radius
 
def areaOfSquare(side):
    return side ** 2 
 
radiusstr= input("Enter radius of circle: ")
radius = int (radiusstr)
print("Area of circle= ", areaOfCircle(radius))
 
sidestr= input("Enterv side of square: ")
side= int (sidestr)
print("Area of square=" , areaOfSquare(side))
