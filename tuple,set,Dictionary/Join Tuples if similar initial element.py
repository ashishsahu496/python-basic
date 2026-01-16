from enum import unique
from importlib.resources import read_text

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

unique=[]
for i in test_list:
    unique.append(i[0])
unique=set(unique)

print(unique)
result=[]
for i in unique:
    result.append([i])
    for j in test_list:
        if j[0]==i:
            result[-1].append(j[1])

print(list(map(tuple, result)))
