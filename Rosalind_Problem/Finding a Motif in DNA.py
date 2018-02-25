# Finding a Motif in DNA

fr = open('rosalind_subs.txt','r')
lines = fr.readlines()

seq = lines[0].strip()
motif = lines[1].strip()

for i in range(len(seq)+1):
           if seq[i:i+len(motif)] == motif :
                      print i+1 ,
           else :
                      pass
           
fr.close()
