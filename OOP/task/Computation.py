from operator import truediv


class Computation:

    def __init__(self):
        pass


 # -------Factorial--------
    def factorical(self,n):
        j=1
        for i in range(1,n+1):
            j=j*i
            return j
# -------Sum of first n number--------
    def naturalSum(self):
        sum=0
        for i in range(1,n+1):
            sum=sum+i
            return sum

# ----------primality of a given integer n ------------

    def testPrime(self,n):
        j=0
        for i in range(1,n+1):
            if n%i==0:
                j=j+1
        if(j==2):
            return True
        else:
            return False

#----------------------  primality of two number -----------------

    def testPrims(self,n,m):
        # initializing the number of common divisor
        commonDiv=0
        for i in range(1,n+1):
            if ( n% i==0 and m%i==0):
                commonDiv=commonDiv+1
            if commonDiv==0:
                print("the number ",n ,"and", m ,"are co-prime")
            else:
                print("the number are not are co-prime")

#------Multiplication table---------------
    def multable(self,n):
        for i in range(1,10):
            print(n,"*",i,"=",n*i)

    def AllMulti(self,n):
        for i in range(1,n+1):
            print("*"*30)
            for j in range(1,11):
                print(i,"*",j,"=",i*j)

    @staticmethod
    def listDiv(n):
        l=[]
        for i in range(1,n+1):
            if n % i==0:
                l.append(i)
        print(l)


    @staticmethod
    def PrimeDiv(n):
        l=[]
        for i in range(2,n+1):
            if n % i==0:
                prime=True
                for j in range(2,i):
                    if i % j==0:
                        prime=False
                        break
                if prime:
                    l.append(i)
        print(l)



obj=Computation()
# print(obj.testPrime(15))
# obj.AllMulti(15)
Computation.listDiv(15)
Computation.PrimeDiv(60)