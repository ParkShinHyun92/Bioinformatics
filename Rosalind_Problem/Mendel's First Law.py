# Mendel's First Law

x = float(raw_input('put AA number: '))
y = float(raw_input('put Aa number: '))
z = float(raw_input('put aa number: '))

s = (x+y+z) * 2

a = (((2*x+y)/s)**2) + ((2*((2*x+y)/s) * (y+2*z)/s))

print a**2
