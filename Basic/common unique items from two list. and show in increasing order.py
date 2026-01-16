num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

l=[]
for i in num1:
    for j in num2:
        if i==j:
            l.append(i)
print(sorted(l))