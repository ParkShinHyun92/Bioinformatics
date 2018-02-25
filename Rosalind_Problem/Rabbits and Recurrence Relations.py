#Rabbits and Recurrence Relations

month = int(raw_input('put the month: '))
rabbits = int(raw_input('put the rabbits: '))

x = [1]
y = [0]
z = [1 * rabbits]


for i in range(month-3):
    z.append((x[i]+y[i])*rabbits)
    y.append(z[i])
    x.append(x[i]+y[i])

print x[-1] + y[-1] + z[-1]
