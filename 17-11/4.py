import math

while True:
    try:
        r = input('Input radius: ')
        r = float(r)
        break
    except ValueError:
        print('raduis must be digit!')
print('Area = ' + str(math.pi*r*r))