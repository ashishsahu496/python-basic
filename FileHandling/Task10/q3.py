

file_name='sample1.txt'
f=open(file_name,'w')

for i in range(1,11,2):
    line= '{}\t{}\n'.format(i,i+1)

    f.writelines(line)
f.close()

with open(file_name,'r') as f:
    lines=f.read().splitlines()

total=0
with open(file_name,'w') as f:
    for line in lines:
        a,b=line.split(sep='\t')
        res=int(a)*int(b)
        total+=res
        f.write('{}\t{}\t{}\n'.format(a,b,res))
    f.write("total\t"+str(total))
