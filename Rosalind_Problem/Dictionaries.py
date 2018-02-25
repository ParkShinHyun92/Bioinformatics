# Dictionaries

fr = open('rosalind_ini6 (1).txt','r')
lines = fr.readlines()

words = lines[0].strip().split(' ')

dic = {}

for word in words:
           if word not in dic.keys():
                      dic[word] = 1
           else:
                      dic[word] += 1
                      
for i in range(len(dic.keys())):
           print dic.keys()[i] , dic.values()[i]

fr.close
