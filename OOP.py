'''Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area( ) and perimeter( ). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area( ) and perimeter( ) methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square, that have the appropriate inheritance relationships. Finally, write a simple program that allows users to create polygons of the
various types and input their geometric dimensions, and the program then
outputs their area and perimeter. For extra effort, allow users to input
polygons by specifying their vertex coordinates and be able to test if two
such polygons are similar.'''
from abc import ABC, abstractmethod
from math import sqrt


class polygon(ABC) :
    def __init__(self, n):
        self.number_of_sides = n

    def get_sides(self):
        return self.number_of_sides

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Triangle(polygon):
    def __init__(self, length_of_side):
        super().__init__(3)
        self.length = length_of_side

    def get_perimeter(self):
        '''return perimeter of triangle'''
        return sum(map(int,self.length)) / 2

    def get_area(self):
        '''return area of triangle'''
        s = self.get_perimeter()
        a, b, c = self.length
        return sqrt(s*(s-a)*(s-b)*(s-c))

class IsoscelesTriangle(Triangle):
    '''Subclass of triangle'''
    def __init__(self, length_of_side):
        super().__init__(length_of_side)


class EquilateralTriangle(Triangle):
    '''Subclass of triangle'''
    def __init__(self, length_of_side):
        super().__init__(length_of_side)


class Pentagon(polygon):

    def __init__(self, length_of_side):
        super().__init__(5)
        self.length_of_side = length_of_side

    def area(self):
        a = int(self.length_of_side[0])
        Area = 1/4 * sqrt(5*(5+2*sqrt(5))) * a**2
        return Area

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        return sum(map(int,self.length_of_side))


class Hexagon(polygon):

    def __init__(self, length_of_side):
        super().__init__(6)
        self.length_of_side = length_of_side

    def area(self):
        a = int(self.length_of_side[0])
        Area = ((3*sqrt(3)) / 2)* (a**2)
        return Area

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        return sum(map(int, self.length_of_side))


class Octagon(polygon):

    def __init__(self, length_of_side):
        super().__init__(8)
        self.length_of_side = length_of_side

    def area(self):
        a = int(self.length_of_side[0])
        Area = 2*(1+sqrt(2))*(a**2)
        return Area

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        return sum(map(int,self.length_of_side))


class Quadrilateral(polygon):

    def __init__(self, length_of_side):
        super().__init__(4)
        self.length_of_side = length_of_side

    def area(self):
        '''area of Quadrilateral'''
        pass

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        return sum(map(int, self.length_of_side))


class Rectangle(Quadrilateral):

    def __init__(self, length_of_side):  # [side1, side2]
        super().__init__(length_of_side)

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        return sum(map(int,self.length_of_side))


class Square(Rectangle):

    def __init__(self, length_of_side):
        super().__init__(length_of_side)

    def area(self):
        x = self.lengths_of_sides[0]
        return x * x

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x = self.lengths_of_sides[0]
        return x * 4

