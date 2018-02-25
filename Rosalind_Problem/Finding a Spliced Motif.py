# Finding a Spliced Motif

# Save dna to List data
dna = []
seq = ''
fr = open('rosalind_sseq.txt','r')
lines = fr.readlines()

for line in lines:
    if '>' in line:
        dna.append(seq)
        seq = ''
    else :
        seq += line.strip()
dna.append(seq) 
dna.remove('')

print dna

fr.close()
