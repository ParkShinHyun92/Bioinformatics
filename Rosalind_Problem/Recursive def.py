#Recursive def

temporary_seq = ''
nucleotide = ['A','T','G','C']

for a in range(3):
    temporary_seq += nucleotide[a]
    for b in range(3):
        temporary_seq += nucleotide[b]
        for c in range(3):
            temporary_seq += nucleotide[c]
            for d in range(3):
                temporary_seq += nucleotide[d]
                print temporary_seq
