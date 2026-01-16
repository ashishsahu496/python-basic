class Bank:

    def __init__(self,name,acc_no,balance):

        self.__name=name
        self.__acc_no=acc_no
        self.__balance=balance


    def deposit(self,amount):
        self.__balance= self.__balance + amount
        print('Deposit amount: ',amount)
        print(' after Deposit : ',self.__balance)

    def withdraw(self,amount):
        if self.__balance<amount:
            print("You don't have enough money")
        else:
            self.__balance=self.__balance-amount
            bankcharge= self.__bankkcharge()
            self.__balance=self.__balance-bankcharge

    def __bankkcharge(self):
        return 0.05 * self.__balance

    def display(self):
        print("Name:",self.__name)
        print("Account No:",self.__acc_no)
        print(" Account Balance:",self.__balance)
        print(" charge of bank for withdrawal:",self.__bankkcharge())


obj=Bank('ashish',2200002,4000)
obj.deposit(1000)
obj.withdraw(1000)
obj.display()
