# Open Reading Frames

ORF = []

# Save sequence
seq = ''
fr = open('rosalind_orf.txt','r')
lines = fr.readlines()
for line in lines:
    if '>' not in line:
        seq += line.strip()
    else:
        pass

# codon_table
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

a = []
b = []
for i in range(len(seq)):
    if seq[i:i+3] == 'ATG':
        a.append(i)

temp_seq = ''
for k in a:
    y = k
    b.append(temp_seq)
    temp_seq = ''
    while True:
        if len(seq[y:y+3]) != 3:
            temp_seq += seq[y:y+3].lower()
            break
        else:
            if codontable[seq[y:y+3]] == '_':
                temp_seq += codontable[seq[y:y+3]]
                break
            else:
                temp_seq += codontable[seq[y:y+3]]
                y += 3
b.append(temp_seq)
b.remove('')

#print orf
for r in b:
    if '_' in r:
        ORF.append(r[0:-1])
    else:
        pass

# Revserse Sequence
reverse_sequence = ''
reverse_seq = {'A':'T','T':'A','G':'C','C':'G'}
for i in range(1,len(seq)+1):
    reverse_sequence += reverse_seq[seq[-i]]

c = []
d = []
for i in range(len(reverse_sequence)):
    if reverse_sequence[i:i+3] == 'ATG':
        c.append(i)

temp_seq = ''
for k in c:
    y = k
    b.append(temp_seq)
    temp_seq = ''
    while True:
        if len(reverse_sequence[y:y+3]) != 3:
            temp_seq += reverse_sequence[y:y+3].lower()
            break
        else:
            if codontable[reverse_sequence[y:y+3]] == '_':
                temp_seq += codontable[reverse_sequence[y:y+3]]
                break
            else:
                temp_seq += codontable[reverse_sequence[y:y+3]]
                y += 3
b.append(temp_seq)
b.remove('')

#print orf
for r in b:
    if '_' in r:
        ORF.append(r[0:-1])
    else:
        pass
ORF = set(ORF)

for i in ORF:
    print i

fr.close()
