import cmath

print('Input coefficients:\n')

while True:
    try:
        a = input('Input a: ')
        a = complex(a)
        break
    except ValueError:
        print('a must be complex!')

while True:
    try:
        b = input('Input b: ')
        b = complex(b)
        break
    except ValueError:
        print('b must be complex!')

while True:
    try:
        c = input('Input c: ')
        c = complex(c)
        break
    except ValueError:
        print('c must be complex!')

d=b*b - 4*a*c

if (d!=0):
    x1=( -b+cmath.sqrt(d) ) / (2*a)
    x2=( -b-cmath.sqrt(d) ) / (2*a)
    if (x1.imag==0):
        x1=x1.real
    if (x2.imag==0):
        x2=x2.real
    print('x1: '+str(x1)+'\nx2:' + str(x2))
else:
    x=complex( -b / (2*a))
    print('x: ' + str(x))