class Rectangle:

    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def __permiter(self):
        return 2 * (self.__length * self.__width)

    def __area(self):
        return self.__length * self.__width

    def display(self):
        print("lenght :", self.__length)
        print("width :", self.__width)
        print("area :", self.__area())
        print("perimeter :", self.__permiter())


obj = Rectangle(4, 5)
obj.display()
