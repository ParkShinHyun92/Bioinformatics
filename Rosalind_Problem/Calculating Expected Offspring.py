# Calculating Expected Offspring

fr = open('rosalind_iev.txt','r')
lines = fr.readlines()

mate = lines[0].strip().split(' ')

expectation_value = (int(mate[0])*1) + (int(mate[1])*1) + (float(mate[2])*1) + (float(mate[3])*3/4) + (float(mate[4])*1/2) + (int(mate[5])*0)

print expectation_value*2

fr.close()
