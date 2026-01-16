# 'maximum dum subarray'

l=[-2,4,7,-1,6,-11,14,3,-1,-6]

d={}

for i in range(0,len(l)):
    subarray=[]
    for j in range(i,len(l)):
        subarray.append(l[j])
        d[sum(subarray)]=subarray

max_val=max(d.keys())

for i in d:
    if i==max_val:
        print(d[i])