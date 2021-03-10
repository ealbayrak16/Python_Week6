"""
Developer: Ersin ÖZTÜRK
Program Name: Area, Perimeter, Volume and Surface Calculation of Triangle, Square, Cube and Pyramid
Date: 10.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes the dimensions and calculate the Area, Perimeter, Volume and Surface

Extra Information:

Create two class named Triangle and Rectangle.
Create a subclass named Square inherited from Rectangle.
Create a subclass named Cube inherited from Square.
Create a subclass named Pyramid multiple inherited both from Triangle and Square.

Two dimensional classes (Triangle, Rectangle and Square) should have:
its dimensions as attributes.(can be inherited from a superclass)
methods which calculate its area and perimeter separately.

Three dimensional classes (Cube and Pyramid) should have:
its dimensions as attributes which are inherited from a superclass
its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately.
(surface area is optional, you may not do this)
"""


from math import sqrt


class Triangle:
    def __init__(self, edge1, edge2, edge3):
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3

    def perimeter(self):
        self.perimeter_triangle = self.edge1 + self.edge2 + self.edge3
        return self.perimeter_triangle

    def area(self):
        s = self.perimeter()/2
        self.area_triangle = sqrt(s*(s-self.edge1)*(s-self.edge2)*(s-self.edge3))
        return self.area_triangle

class Rectangle:
    def __init__(self, edge1, edge2):
        self.edge1 = edge1
        self.edge2 = edge2

    def perimeter(self):
        self.perimeter_rectangle = 2*(self.edge1 + self.edge2)
        return self.perimeter_rectangle

    def area(self):
        self.area_rectangle = self.edge1 * self.edge2
        return self.area_rectangle



class Square(Rectangle):
    def __init__(self,edge):
        super().__init__(edge,edge)


class Cube(Square):
    def __init__(self,height):
        super().__init__(height)
        self.height=height

    def volume(self):

        self.volume_cube = Square.area(self)*self.height
        return self.volume_cube

    def surface_cube(self):
        self.surface_cube_var=6*Square.area(self)
        return self.surface_cube_var


class Pyramid(Triangle,Square):
    def __init__(self, height_pyra, edge_pyra_sqr):
        self.height_pyra=height_pyra
        a=sqrt((edge_pyra_sqr * sqrt(2) / 2) ** 2 + height_pyra ** 2)
        Triangle.__init__(self, edge_pyra_sqr, a, a)
        Square.__init__(self, edge_pyra_sqr)

    def volume(self):
        self.volume_pyra=(1/3)*(Square.area(self)*self.height_pyra)
        return self.volume_pyra

    def surface(self):
        self.surface_pyra=Square.area(self)+4*Triangle.area(self)
        return self.surface_pyra


list_triangle = input("Please enter the triangle edges with hypent (EXAMPLE: 3-4-5): ").split("-")
list_triangle = [int(i) for i in list_triangle]
obj_triangle=Triangle(list_triangle[0],list_triangle[1],list_triangle[2])
print(f"The Perimeter of Triangle is {obj_triangle.perimeter()}")
print(f"The Area of Triangle is {obj_triangle.area()}")

print("=================")

list_rectangle = input("Please enter the rectangle edges with hypent (EXAMPLE: 3-4): ").split("-")
list_rectangle = [int(i) for i in list_rectangle]
obj_rectangle = Rectangle(list_rectangle[0],list_rectangle[1])
print(f"The Perimeter of Rectangle is {obj_rectangle.perimeter()}")
print(f"The Area of Rectangle is {obj_rectangle.area()}")

print("=================")

square_edge = int(input("Please enter the square edge (EXAMPLE: 5): "))
obj_square = Square(square_edge)
print(f"The Perimeter of Square is {obj_square.perimeter()}")
print(f"The Area of Square is {obj_square.area()}")

print("=================")

cube_edge = int(input("Please enter the cube edge (EXAMPLE: 5): "))
obj_cube = Cube(cube_edge)
print(f"The Volume of Cube is {obj_cube.volume()}")
print(f"The Surface Area of Cube is {obj_cube.surface_cube()}")

print("=================")

list_pyramid = input("Please enter the pyramid floor edges and height with hypent (EXAMPLE: 3-4): ").split("-")
list_pyramid = [int(i) for i in list_pyramid]
obj_pyramid = Pyramid(list_pyramid[0],list_pyramid[1])
print(f"The Volume of pyramid is {obj_pyramid.volume()}")
print(f"The Surface Area of Pyramid is {round(obj_pyramid.surface(),2)}")






