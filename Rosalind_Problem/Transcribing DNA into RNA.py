# Transcribing DNA into RNA

fr = open('rosalind_rna.txt','r')
lines = fr.readlines()

string =lines[0].strip()

for i in range(string.count('T')):
           string = string.replace('T','U')

print string

fr.close()
