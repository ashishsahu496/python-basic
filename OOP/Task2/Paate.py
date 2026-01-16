import random
class Card:

    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

    def __repr__(self):
        return '{} ->{}'.format(self.suit,self.value)

class Deck:

    def __init__(self):
        suits=['Hearts','Diamond','Club','Spade']
        values=['2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen','King','Ace']
        self.cards=[Card(suit,value) for suit in suits for value in values]

        # print(self.cards)
        # print(len(self.cards))

    def __str__(self):
        return 'Cards Left' +str(len(self.cards))


    def Shuffle(self):
        if len(self.cards) < 52 :
            print("only full deck cards can be shuffled")

        else:
            random.shuffle(self.cards)
            return self.cards

    def deal(self):
        if len(self.cards)==0:
            print("no cards left")
        return self.cards.pop()

obj = Deck()
obj.Shuffle()
print(obj.deal())
print(obj.deal())
print(obj)