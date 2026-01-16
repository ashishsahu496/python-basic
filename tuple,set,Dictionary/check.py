list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

out=[0,0,0]

for i in list1:
    if type(i)==list:
        out[0] = out[0] + 1
    elif type(i) == tuple:
        out[1] = out[1] + 1
    elif type(i) == set:
        out[2] = out[2] + 1


    else:
        pass
print('List-{}\nSet-{}\nTuple-{}'.format(out[0],out[1],out[2]))