decimal=5

def decTobin(decimal):
    if decimal==0:
        return "0"
    else:
        return decTobin(decimal >> 1) + str(decimal & 1)

print(decTobin(decimal))