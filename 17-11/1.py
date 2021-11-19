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

print('Inputed: ' + str(a), str(b))

print('a + b: ' + str(a + b))
print('a - b: ' + str(a - b))
print('a * b: ' + str(a * b))
print('a / b: ' + str(a / b))
print('a ^ b: ' + str(a ** b))
print('a % b: ' + str(a % b))
print('div(a, b): ' + str(a // b))