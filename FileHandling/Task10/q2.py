

def vowel_count_table(filename):
    vowels =['a','e','i','o','u']
    d={i :0 for i in vowels}

    for current_line in open(filename,'r'):
        for ch in current_line:
            if ch in vowels:
                d[ch]+=1

    return d

print(vowel_count_table('sample.txt'))


