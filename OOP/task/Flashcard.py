import random
class Flashcard:
    def __init__(self):
        self.__fruit={
            "Banana": "yellow",
            "Strawberries": "pink",
            "Apple":"red",
            "Graphs":"green"
        }

    def quiz(self):

        while True:
            fruit,color=random.choices(list(self.__fruit.items()))[0]

            print("what is color of {} ".format(fruit))
            user_in=input()

            if user_in==color:
                print("sahi jabab")
            else:
                print("galat jabab")

                option=int(input("enter the 0 for continue to play else press 1 for exit "))
                if option:
                    break

print("Welcome to Flashcard play game")
obj=Flashcard()
obj.quiz()