t1 = (0,1,2,3)
t2 = (0,1,2,3)

flag=True

for i,j in zip(t1,t2):
    if i==j:
        continue
    else:
        flag=False
        break
if flag:
    print('same')
else:
    print('not same')
