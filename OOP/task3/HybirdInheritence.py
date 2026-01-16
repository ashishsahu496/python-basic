class Bill:

    def __init__(self,Items,price):
        self.Items=Items
        self.price=price
        self.total=0

        for i in self.price:
            self.total+=i

    def dislpay(self):
        print("Item   \t  \t \t ====>   price")

        for i in range(len(self.Items)):
            print(self.Items[i],'\t' , '\t' ,'\t','====>',self.price[i],'\t')
            print('*'*10)
            print('total',self.total)

# items=['External HD','Pen Drive','Printer','Ram']
# price=[4000,600,15000,8000]
# obj=Bill(items,price)
# obj.dislpay()

class CashPayment(Bill):

    def __init__(self,Items,price,deno,value):
        super().__init__(Items,price)
        self.deno=deno
        self.value=value

    def show_cash_payment(self):
        super().dislpay()

        for i in range(len(self.deno)):
            print(self.deno[i] ,'*', self.value[i],'==',self.deno[i]*self.value[i])


# deno=[10,20,50,100,200,500,2000]
# value=[1,2,1,2,4,5,3]
#
# items=['External HD','Pen Drive','Printer','Ram']
# price=[4000,600,15000,8000]
# obj=CashPayment(items,price,deno,value)
# obj.show_cash_payment()


class ChequePayment(Bill):
    def __init__(self,Items,price,cno,bname):
        super().__init__(Items,price)
        self.cno=cno
        self.bname=bname


    def show_cheque_payment(self):
        super().dislpay()
        print('cno',self.cno)
        print('bname',self.bname)

items=['External HD','Pen Drive','Printer','Ram']
price=[4000,600,15000,8000]
option=int(input("Enter your choice: for cash payment press 1 and for cheque payment press 2: "))
if option==1:
    deno=[10,20,50,100,200,500,2000]
    value=[1,2,1,2,4,5,3]
    obj=CashPayment(items,price,deno,value)
    obj.show_cash_payment()

elif option==2:
    name=input("Enter the bank name: ")
    cno=input("Enter the cheque number: ")
    obj=ChequePayment(items,price,cno,name)
    obj.show_cheque_payment()

else:
    print("Invalid choice")
    exit()






