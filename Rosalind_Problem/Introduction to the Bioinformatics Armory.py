#Introduction to the Bioinformatics Armory

fr = open('rosalind_ini.txt','r')
lines = fr.readlines()

print '%d %d %d %d' %(lines[0].count('A'),lines[0].count('C'),lines[0].count('G'),lines[0].count('T'))

fr.close()
