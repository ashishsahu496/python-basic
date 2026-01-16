import random


class ValueTooLarge(Exception):
    def display(self):
        print("Value too large")

class ValueTooSmall(Exception):
    def display(self):
        print("Value too Small")

class GuessError(Exception):
    def display(self):
        print("GuessError")

num= random.randint(1,100)
count=0

while True:
    try:
        count += 1
        guess=int(input("Guess a number between 1 and 100: "))
        if guess<1:
            raise GuessError
        if guess==num:
            print("great you succeeded")
            count+=1
            break
        if guess>num:
            raise ValueTooLarge
        if guess<num:
            raise ValueTooSmall
    except ValueTooLarge as l:
        l.display()
    except ValueTooSmall as s:
        s.display()
    except GuessError as g:
        g.display()

print(count)