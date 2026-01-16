
input_file="sample.txt"
output_file="sample_reversed.txt"

def reverse_line(infilemname,outfilename):
    with open(infilemname,"r") as infile , open(outfilename,"w") as outfile:
        for one_line in infile:
            outfile.write(one_line.rstrip()[::-1]+'\n')

reverse_line("sample.txt","sample_reversed.txt")



