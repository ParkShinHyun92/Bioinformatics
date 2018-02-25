# Finding a Spliced Motif

fr = open('rosalind_sseq.txt','r')
lines = fr.readlines()

string = lines[0].strip()

sequences = []
sequence = ''

for line in lines:
    if '>' in line:
        sequences.append(sequence)
        sequence = ''
    else :
        sequence += line.strip()
        
sequences.append(sequence)
del(sequences[0])

sequence = sequences[0]
motif = sequences[1]

motif = motif + 'H'

print motif

indexs = []

print len(motif)

k = 0

for index in range(len(sequence)-1):
    if sequence[index] == motif[k] and k < len(motif):
        indexs.append(index+1)
        k += 1
print len(indexs)

for index in indexs:
    print index, 
