# Working with Files

fr = open('rosalind_ini5.txt','r')
lines = fr.readlines()

print lines

for i in range(1,len(lines),2):
    print lines[i].strip()

fr.close
