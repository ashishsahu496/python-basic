

def edit_distance(word1,word2):
    if len(word1)==0:
        return len(word2)
    elif len(word2)==0:
        return len(word1)
    else:
        cost=0
        if word1[-1]!=word2[-1]:
            cost=1
        d1=edit_distance(word1[:-1],word2)+1
        d2=edit_distance(word2[:-1],word1)+1
        d3=edit_distance(word1[:-1],word2[:-1]) + cost

print(edit_distance("kitten","sitting"))

