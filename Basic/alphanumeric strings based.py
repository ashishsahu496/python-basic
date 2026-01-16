'''###`Problem 7:` Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
'''

val=['1ac21', '23fg', '456', '098d','1','kls']
p=[]
for item in val:
    product = 1
    for char in item:
        if char.isdigit():
            product*=int(char)
            p.append(product)
print(p)
t={"",}
for i in p:
    t.add(i)
print(t)
