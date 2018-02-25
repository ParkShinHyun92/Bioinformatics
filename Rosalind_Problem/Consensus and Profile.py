# Consensus and Profile

# read sequnence part
fr = open('rosalind_cons.txt','r')
lines = fr.readlines()

fr.close()

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

# set nucleotide list
Adenine = [0]*len(sequences[0])
Guanine = [0]*len(sequences[0])
Cytosine = [0]*len(sequences[0])
Thymine = [0]*len(sequences[0])

for sequence in sequences:
    for index in range(len(sequence)):
        if sequence[index] == 'A':
            Adenine[index] = Adenine[index] + 1
        elif sequence[index] == 'G':
            Guanine[index] = Guanine[index] + 1
        elif sequence[index] == 'C':
            Cytosine[index] = Cytosine[index] + 1
        else:
            Thymine[index] = Thymine[index] + 1

# print result
sequence = ''
for index in range(len(sequences[0])): 
    if Adenine[index] == max(Adenine[index],Guanine[index],Cytosine[index],Thymine[index]):
        sequence = sequence + 'A'
    elif Guanine[index] == max(Adenine[index],Guanine[index],Cytosine[index],Thymine[index]):
        sequence = sequence + 'G'
    elif Cytosine[index] == max(Adenine[index],Guanine[index],Cytosine[index],Thymine[index]):
        sequence = sequence + 'C'
    else:
        sequence = sequence + 'T'
print sequence

count_Adenine = "A: "
for count in Adenine:
    count_Adenine = count_Adenine + str(count) + ' '
count_Cytosine = "C: "
for count in Cytosine:
    count_Cytosine = count_Cytosine + str(count) + ' '
count_Guanine = "G: "
for count in Guanine:
    count_Guanine = count_Guanine + str(count) + ' '
count_Thymine = "T: "
for count in Thymine:
    count_Thymine = count_Thymine + str(count) + ' '
print count_Adenine
print count_Cytosine
print count_Guanine
print count_Thymine
