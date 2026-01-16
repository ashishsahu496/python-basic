'''Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -
Write a program to show no. of items of each candy type.'''

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no = [10,20,34,74,32]
l2=[]
for i in no:
    l2.append(int(i))

for i in list(zip(candy_list, l2)):
    print(i)