l=[2,4,6,10,1]

l1=[]
for i in l:
    sum = 0
    for j in l:
            if j>=i:
                sum=sum+j
    l1.append(sum)

print(l1)