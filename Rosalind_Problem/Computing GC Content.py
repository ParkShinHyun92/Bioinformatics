#Computing GC Content

fr = open('rosalind_gc.txt','r')
lines = fr.readlines()

fr.close()

dna_name = {}
sequence = ''
title = ''
ratios = []

for line in lines:
    if '>' in line:
        dna_name[title] = sequence
        sequence = ''
        title = line.strip()
    else :
        sequence += line.strip()
        
dna_name[title] = sequence
del dna_name['']                                            # erase First dictionary & save last dictionary


sequence_2 = dna_name.values()                              # Make value's list

for seq in sequence_2:                                      #calculate ratio
    GC_count = seq.count('G') + seq.count('C')
    ratios.append(GC_count/float(len(seq))*100)

max_ratio = 0

for ratio in ratios:                                        #select max_value
    if max_ratio >= ratio:
        pass
    else:
        max_ratio = ratio
        
#print max(ratios)
        
for i in range(len(dna_name)):                              #select DNA Key
    if ratios[i] == max_ratio:
        print dna_name.keys()[i].replace('>','')
    else:
        pass
    
print max_ratio
