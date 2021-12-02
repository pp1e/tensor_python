def fibonacciNumber(number):
    if (number==1):
        return 0
    if (number==2):
        return 1
    return fibonacciNumber(number-1)+fibonacciNumber(number-2)

while True:
        try:
            number = input('Input ordinal number: ')
            number = int(number)
            if (number<1):
                raise ValueError
            break
        except ValueError:
            print('Ordinal number must be positive integer!')
print(str(number)+'-th Fibonacci number: '+str(fibonacciNumber(number)))        