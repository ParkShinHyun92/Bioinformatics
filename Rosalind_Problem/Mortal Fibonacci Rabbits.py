# Mortal Fibonacci Rabbits

month = int(raw_input('enter the month:'))
death  = int(raw_input('enter death month:'))

new_month = [1]
last_month = [0]

for i in range(death-1):
    new_month.append(0)
    last_month.append(0)

for i in range(0,month):
    for t in range(len(new_month)):
        last_month[t] = new_month[t]

    for u in range(1,death):
        new_month[0] += last_month[u]
    new_month[0] -= last_month[0]
    
    for k in range(1,death):
        new_month[k] = last_month[k-1]
    
sum = 0
for i in last_month:
    sum += i
print sum
