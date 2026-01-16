class Student:

    def __init__(self):
        self.__sid=None
        self.__marks=None
        self.__age=None

    def set_sid(self,sid):
        self.__sid=sid
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age

    def get_sid(self):
        return self.__sid
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks


    def valid_age(self):
        return self.__age>20

    def validate_marks(self):
        return 0 <= self.__marks <= 100

    def check_qualification(self):
        if self.valid_age() and self.validate_marks():
            return self.__marks >=65
        else:
            return False


s1=Student()
s1.set_sid(1)
s1.set_age(20)
s1.set_marks(40)
print(s1.get_sid(),"sid",s1.get_age(),"age",s1.get_marks(),"marks")
print(s1.check_qualification())



