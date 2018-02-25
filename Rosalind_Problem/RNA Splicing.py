# RNA Splicing

# Save dna to List data
dna = []
seq = ''
fr = open('rosalind_splc.txt','r')
lines = fr.readlines()

for line in lines:
    if '>' in line:
        dna.append(seq)
        seq = ''
    else :
        seq += line.strip()
dna.append(seq) 
dna.remove('')

# Remove intron in Seq

for i in range(1,len(dna)):
    if dna[i] in dna[0]:
        k = dna[0].find(dna[i])
        dna[0] = dna[0][:k] + dna[0][k+len(dna[i]):]

print len(dna[0])

# Make to codon
codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
codon = ''
for u in range(0,len(dna[0]),3):
    codon += codontable[dna[0][u:u+3]]

print codon[:-1]

fr.close()
