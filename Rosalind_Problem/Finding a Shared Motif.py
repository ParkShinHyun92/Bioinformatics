# Finding a Shared Motif

#save dna to dictionary data
fr = open('rosalind_lcsm.txt','r')
lines = fr.readlines()
dna = {}
title = ''
seq = ''
for line in lines:
    if '>' in line:
        dna[title] = seq
        title = line.strip()
        seq = ''
    else :
        seq += line.strip()
del dna['']

print len(dna.values())
print len(dna.values()[0])


# Make motif
a = []
motif = ''
for i in range(len(dna.values()[0])):
    for c in range(len(dna.values()[0])+1):
        if dna.values()[0][i:c] != '':
            a.append(dna.values()[0][i:c])
        else:
            pass

motif = []

# select motif
for h in range(len(a)):
    k = 0
    while a[h] in dna.values()[k]:
        k = k+1
        if k > len(dna.values())-1:
            motif.append(a[h])
            break
        else:
            pass
print len(motif)

# Choose longest motif
longest_motif = ''
for u in range(len(motif)):
    if longest_motif == '':
        longest_motif = motif[u]
    elif len(motif[u])>len(longest_motif):
        longest_motif = motif[u]
    else:
        pass
print longest_motif
fr.close()
