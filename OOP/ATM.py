class ATM :
    def __init__(self):
       self.pin=''
       self.balance=0
       self.menu()

    def menu(self):
        user_input=input('''
        Hi, how can i help you?
        1.press 1 for create pin
        2.press 2 for change pin
        3.press 3 for check balance
        4.press 4 for withdrawal
        5 anything for exit
        ''')
        if user_input == '1':
            self.create_pin()

        elif user_input == '2':
            self.change_pin()

        elif user_input == '3':
            self.check_balance()

        elif user_input == '4':
            self.withdrawal()

        else:
            exit()



    def create_pin(self):
        user_pin = input('Enter pin number: ')
        self.pin = user_pin

        user_balance = input('Enter balance: ')
        self.balance = user_balance

        print('Pin created successfully !')
        self.menu()


    def change_pin(self):
        user_pin = input('Enter pin number: ')
        if user_pin == self.pin  :
            new_pin = input('Enter new pin number: ')
            self.pin = new_pin
            print('Pin changed successfully !')
            self.menu()

        else:
            print('nahi kr de sakta change ')
            self.menu()



    def check_balance(self):
        user_pin = input('Enter pin number: ')
        if user_pin == self.pin :
            print('your balance is: ',self.balance)
            self.menu()

        else:
            print('sahi pin dal')
            self.menu()


    def withdrawal(self):
        user_pin = input('Enter pin number: ')
        if user_pin == self.pin :
            amount=int(input('Enter amount: '))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Your withdarwal is successfull: ',amount)


            else:
                print('low balance')

        else:
            print('wrong pin')
            self.menu()



obj = ATM()
