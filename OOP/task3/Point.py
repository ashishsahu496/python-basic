class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show_point(self):
        return '{},{}'.format(self.x,self.y)

class Location:

    def __init__(self,x1,y1,x2,y2):
       self.source=Point(x1,y1)
       self.destination=Point(x2,y2)

    def show(self):
        print("source is ",self.source.show_point())
        print("destination is ",self.destination.show_point())

    def reflection(self):
        self.destination.y= -self.destination.y
        print("reflection is ",self.destination.show_point())

L=Location(-1,0,1,2)
L.show()
L.reflection()