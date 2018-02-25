# Variables and Some Arithmetic

fr = open('rosalind_ini2.txt','r')
lines = fr.readlines()

numbers = lines[0].strip().split(' ')

print int(numbers[0])**2 + int(numbers[1])**2

fr.close

