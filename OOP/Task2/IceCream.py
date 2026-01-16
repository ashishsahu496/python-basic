class Scoop:

    __counter=0

    def __init__(self,flavor,num_scoop=1):
        self.num_scoop=num_scoop
        self.flavor=flavor
        self.__price=None
        Scoop.__counter+=1


    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return self.__price

    def __str__(self):
        return "Flavor - {} and Price -{}".format(self.flavor,self.__price)

    @staticmethod
    def sold():
        return Scoop.__counter

class Bowl:

    __counter=0
    def __init__(self,max_scoop=3):
        self.__scoopList=[]
        Bowl.__counter+=1
        self.scoop_added=0
        self.max_scoop=max_scoop

    def add_scoops(self,*new_scoop):
        for scoop in new_scoop:
            if self.scoop_added + scoop.num_scoop <= self.max_scoop:
                self.__scoopList.append(scoop)
                self.scoop_added =self.scoop_added + scoop.num_scoop
                print(scoop.flavor,"Added !")
            else:
                print("Bowl is full")
                break


    def display(self):
        total=0
        for scoop in self.__scoopList:
            print(scoop)
            total=total+scoop.get_price()

        print("Total scoops :",total)

    @staticmethod
    def sold():
        return Bowl.__counter

# choco = Scoop('chocolate')
# print(choco)
# choco.set_price(100)
#
# berry = Scoop('berry')
# berry.set_price(120)
# print(berry)
#
# vanilla = Scoop('vanilla')
# vanilla.set_price(150)
#
# bowl = Bowl()
# bowl1 = Bowl()
#
# bowl.add_scoops(choco) # Giving one parameter
# bowl.add_scoops(berry, vanilla) # Multiple
# # add_scoops should handle both scenerios
#
# print(bowl)
#
# bowl.display()
#
# print(Scoop.sold())
# print(Bowl.sold())
choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)


berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla') # no of scoop parameter not given, will take default value
vanilla.set_price(150)
print(vanilla)

bowl1 = Bowl() # max_scoop parameter not given, will take default value
bowl1.add_scoops(choco) # Giving one parameter
bowl1.add_scoops(berry, vanilla) # Multiple
bowl1.display()