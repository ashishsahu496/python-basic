l1=[1,2,3,4,5,1]
l2=[2,3,5,7,8]
l3=[]

for item in l1:
    if item not in l3:
        l3.append(item)

for item in l2:
    if item not in l3:
        l3.append(item)

print(l3)