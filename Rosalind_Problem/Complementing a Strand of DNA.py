#Complementing a Strand of DNA

fr = open('rosalind_revc.txt','r')
lines = fr.readlines()
seq =lines[0].strip()

reverse_DNA = {'A':'T','T':'A','C':'G','G':'C'}

recersed_sequence = ''

for d in range (len(seq)):
    recersed_sequence += reverse_DNA[seq[-d-1]]
               
print recersed_sequence
fr.close
