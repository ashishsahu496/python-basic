class Instructor:

    def __init__(self,name,technology,experience,feedback):
        self.__name=name
        self.__technology=technology
        self.__experience=experience
        self.__feedback=feedback


    def check_eligibility(self):

        if self.__experience>3 and self.__feedback >=4.5 :
            return True
        elif self.__experience<=3 and self.__feedback>=4 :
            return True
        else:
            return False


    def allocate_course(self,technology):

        eligibility=self.check_eligibility()

        if eligibility:
            if technology in self.__technology:
                return "Padha Sakta hai"
            else:
                return "ye toh usko aata he nhi hai"
        else:
            return "accha nhi padta"

ins=Instructor("rajesh",['Data Science','JAVA',"Python"],3,4)
print(ins.allocate_course('JAVA'))