# Strings and Lists

fr = open('rosalind_ini3.txt','r')
lines = fr.readlines()

string =lines[0].strip()
positions = lines[1].strip()
position = positions.split()
print string
print string[int(position[0]):int(position[1])+1],string[int(position[2]):int(position[3])+1]

fr.close()
