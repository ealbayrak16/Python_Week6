class Triangle:
    def __init__(self,a_length, b_length, c_lenght, a_lenght_height):
        self.a_length = a_length
        self.b_lenght = b_length
        self.c_lenght = c_lenght
        self.a_length_height = a_lenght_height
    def area(self):
        area = self.a_length * self.a_length_height / 2
        return f"area = {area}"
    def perimeter(self):
        primeter = self.a_length + self.b_lenght + self.c_lenght
        return f"primeter = {primeter}"

class Rectangle:
    def __init__(self,a_length, b_length):
        self.a_length = a_length
        self.b_lenght = b_length
    def area(self):
        area = self.a_length * self.b_lenght
        return f"Area = {area}"
    def perimeter(self):
        primeter = 2 * (self.a_length + self.b_lenght)
        return f"primeter = {primeter}"

class Square(Rectangle):
    def __init__(self, a_length):
        super().__init__(a_length, a_length)
    def area(self):
        area = self.a_length**2
        return f"area = {area}"
    def perimeter(self):
        primeter = 4 * self.a_length
        return f"primeter = {primeter}"

class Cube(Square):
    def __init__(self, a_length):
        super().__init__(a_length)
    def area(self):
        area = 6*self.a_length**2
        return f"area = {area}"
    def primeter(self):
        primeter = 24 * self.a_length
        return f"primeter = {primeter}"
    def volume (self):
        volume = self.a_length ** 3
        return f"volume = {volume}"

class Pyramid(Triangle, Square):
    def __init__(self, a_length, b_length, c_lenght, a_lenght_height):
        super().__init__(a_length, b_length, c_lenght, a_lenght_height)
    def area(self):
        area = self.a_length * (self.a_length+(((self.a_length**2) + (4*self.a_length_height**2))**0.5))
        return f"area = {area}"
    def volume(self):
        volume = ((self.a_length**2) * self.a_length_height)/3
        return f'volume : {volume}'

üçgen = Triangle(3,4,5,6)
print(üçgen.area())
print(üçgen.perimeter())
print("--------------------------------------------")
dikdörtgen = Rectangle (3, 4)
print(dikdörtgen.area())
print(dikdörtgen.perimeter())
print("--------------------------------------------")
kare = Square(3)
print(kare.area())
print(kare.perimeter())
print("--------------------------------------------")
küp = Cube(3)
print(küp.area())
print(küp.primeter())
print(küp.volume())
print("--------------------------------------------")
piramit = Pyramid(3, 4,  5 , 6)
print(piramit.area())
print(piramit.volume())
