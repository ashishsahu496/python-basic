import numpy as np

# i. Add marks every student of an extra subject in the same array.
# ii. Add two new students marks in respective 5 subjects.(one subject added in above task)
# iii. Add extra column with sum of all subjects(5-subjects) marks
# iv. Sort the array(non-ascending order) on total marks column--one added in above task. Show top 2 rows.

marks=np.array([[13, 10,  9, 33],
       [63, 46, 90, 42],
       [39, 76, 13, 29],
       [82,  9, 29, 78],
       [67, 61, 59, 36]])
# print(marks)
extra_subject = np.array([41, 87, 72, 36, 92]).reshape(-1,1)
# print(extra_subject)
m1=np.concatenate([marks,extra_subject], axis=1)
# print(marks)
rec1 = np.array([77, 83, 98, 95, 89]).reshape(1,-1)
rec2 = np.array([92, 71, 52, 61, 53]).reshape(1,-1)
# print(rec1)
m2=np.concatenate([m1,rec1, rec2], axis=0)
# print(m2)

sum_of_stud=m2.sum(axis=1,keepdims=True)
# print(sum_of_stud)
m3=np.concatenate([m2,sum_of_stud], axis=1)
print(m3)
print(np.array(sorted(m3,key=lambda x:x[-1], reverse=True)))