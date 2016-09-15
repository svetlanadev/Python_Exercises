import math

username = raw_input('What is your name?  ')
print username,', input the quadratic equation coefficients: a, b, c for ax2+bx+c=0'
a = float(input('a =  '))
b = float(input('b =  '))
c = float(input('c =  '))

D = (b * b) - (4 * a * c)
print 'Discriminant D = ', D
if D < 0:
	print 'The equation has no roots'
if D == 0:
	x = (- b - math.sqrt(D)) / (2 * a)
	print x
if D > 0:
	x1 = (- b - math.sqrt(D)) / (2 * a)
	x2 = (- b + math.sqrt(D)) / (2 * a)
	print x1, x2
