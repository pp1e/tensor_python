import math

print('Input coefficients:\n')

while True:
    try:
        a = input('Input a: ')
        a = float(a)
        break
    except ValueError:
        print('a must be digit!')

while True:
    try:
        b = input('Input b: ')
        b = float(b)
        break
    except ValueError:
        print('b must be digit!')

while True:
    try:
        c = input('Input c: ')
        c = float(c)
        break
    except ValueError:
        print('c must be digit!')

d = b*b - 4*a*c

if (d > 0):
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print('x1: ' + str(x1) + '\nx2:' + str(x2))
elif (d == 0):
    x = -b / (2*a)
    print('x: ' + str(x))
else:
    print('No roots')