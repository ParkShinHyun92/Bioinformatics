# Transitions and Transversions

# Save dna to List data
dna = []
seq = ''
fr = open('rosalind_tran.txt','r')
lines = fr.readlines()

for line in lines:
    if '>' in line:
        dna.append(seq)
        seq = ''
    else :
        seq += line.strip()
dna.append(seq)
dna.remove('')

# Count Ti,Tv
Ti = 0
Tv = 0
for i in range(len(dna[0])):
    if dna[0][i] == 'A' and dna[1][i] == 'G' or dna[0][i] == 'G' and dna[1][i] == 'A' or dna[0][i] == 'T' and dna[1][i] == 'C' or dna[0][i] == 'C' and dna[1][i] =='T':
        Ti += 1
    elif dna[0][i] == dna[1][i]:
        pass
    else:
        Tv += 1
    
print '%f' %(float(Ti)/Tv)

fr.close()
