l=[1,22,13,7,9,11,10]
s=16

for i in range(0,len(l)):
    sum_arr=[]
    for j in range(i,len(l)):
        sum_arr.append(l[j])

        # print(sum_arr,sum(sum_arr))
        if sum(sum_arr)==s:
            print(sum_arr)