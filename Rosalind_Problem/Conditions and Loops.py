# Conditions and Loops

fr = open('rosalind_ini4.txt','r')
lines = fr.readlines()

numbers = lines[0].strip().split(' ')

sum_odd = 0

for i in range(int(numbers[0]),int(numbers[1])+1,2):
           sum_odd += i

print sum_odd

fr.close
