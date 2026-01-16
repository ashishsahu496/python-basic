from fractions import Fraction


class Fraction:
    def __init__(self,x,y):
        self.num=x
        self.den=y


    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        new_num=self.num*self.den+other.num*self.den
        new_den=other.den*self.den
        return Fraction(new_num,new_den)

    def __sub__(self,other):
        new_num=self.num*self.den-other.num*self.den
        new_den=other.den*self.den
        return Fraction(new_num,new_den)

    def __mul__(self,other):
        new_num=self.num * other.num
        new_den=self.den * other.den
        return Fraction(new_num,new_den)

    def __truediv__(self,other):
        new_num=self.num * other.den
        new_den=self.num * other.den
        return Fraction(new_num,new_den)

p1=Fraction(1,2)
p2=Fraction(3,4)
print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1/p2)

