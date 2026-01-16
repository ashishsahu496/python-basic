t=(1, 5, 7, 8, 10)
l=[]
l.append(t[0]*t[1])

for i in range(1,len(t)-1):
    l.append(t[i]*t[i-1] + t[i]*t[i+1])


l.append(t[-1]*t[-2])
print(tuple(l))
