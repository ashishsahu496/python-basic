import numpy as np

#  Write a program implement Boradcasting Rule to check if two array can be added or not.

# Align both shape
# loop for both shape from behind
# if two number are not equal and none of the number is 1 , return false
# else return true

def checkBroadCast(a,b):
    a=a[::-1]
    b=b[::-1]
    for ai , bi in zip(a,b):
        if ai != bi and ai !=1 and bi !=1:
            return False
    return True

print(checkBroadCast((4,3,3,5),(2,5)))