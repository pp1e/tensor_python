import math

def quad_eq(a, b, c):
    if (a == 0):
        if (b == 0):
            return 'No roots'
        x = -c / b
        return x

    d = b*b - 4*a*c

    if (d > 0):
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)
    elif (d == 0):
        x = -b / (2*a)
        return x
    else:
        return 'No roots'