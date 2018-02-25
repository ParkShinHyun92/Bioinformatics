# Counting Point Mutations

fr = open('rosalind_hamm.txt','r')
lines = fr.readlines()

raw_sequence = lines[0].strip()
mutation_sequence = lines[1].strip()

count = 0

for i in range(len(raw_sequence)):
           if raw_sequence[i] != mutation_sequence[i] :
                      count += 1
           else :
                      pass
           
print count

fr.close()
