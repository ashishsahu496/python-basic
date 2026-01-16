

def gcd(a,b):
    if a==b :
        return a
    elif a>b :
        return (a-b, b)
    else :
        return (b-a, b)

value=gcd(16,24)
print(type(value))
