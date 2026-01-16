import datetime
class ProductExpireOrNot:

    def __init__(self):
        self.manufacture_date= input("enter the manufacture date (DD/MM/YYYY) :")
        self.expiration_date= input("enter the expiration date (DD/MM/YYYY) :")

        self.manufacture_date=datetime.datetime.strptime(self.manufacture_date, "%d/%m/%Y")
        self.expiration_date=datetime.datetime.strptime(self.expiration_date, "%d/%m/%Y")

    def time_to_exipre(self):
        today=datetime.datetime.now()

        if today > self.expiration_date:
            print("product already expired")
        else:
            time_Left =self.expiration_date.date() - today.date()
            print("time left for product to expire : ",time_Left)


obj = ProductExpireOrNot()
obj.time_to_exipre()