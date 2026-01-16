class Rectangle:

    def __init__(self,l,b):
        self.l=l
        self.b=b
        print("inside constructor")

    @classmethod
    def property(cls,ln,bre):
        print("inside method")
        return cls(ln,bre)

    def area(self):
        return   self.l*self.b


    def isSquare(self):
        return True if self.l==self.b else False



obj=Rectangle.property(3,4)
print(obj.area())
print(obj.isSquare())