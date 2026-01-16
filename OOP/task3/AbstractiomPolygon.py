from abc import ABC, abstractmethod



class PolyGon(ABC):

    @abstractmethod
    def get_data():
        pass


    @abstractmethod
    def area():
        pass

class Rectangle(PolyGon):

    def get_data(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

class Triangle(PolyGon):

    def get_data(self,h,b):
        self.h=h
        self.b=b

    def area(self):
        return 0.5 * self.h*self.b


rec=Rectangle()
rec.get_data(3,4)
print(rec.area())

tri=Triangle()
tri.get_data(3,4)
print(tri.area())