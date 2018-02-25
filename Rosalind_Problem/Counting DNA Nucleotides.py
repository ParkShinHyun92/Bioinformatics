# Counting DNA Nucleotides

fr = open('rosalind_dna.txt','r')

lines = fr.readlines()

string =lines[0].strip()

print string.count('A') , string.count('C') , string.count('G') , string.count('T')

fr.close()
