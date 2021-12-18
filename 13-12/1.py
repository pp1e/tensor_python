import math
import time

def time_decorator(func):
    def wrapper(a, b, c):
        launch_time = time.perf_counter()
        func(a, b, c)
        print('Execute time: ' + str(time.perf_counter() - launch_time))
    return wrapper

def log_decorator(func):
    def wrapper(a, b, c):
        func(a, b, c)
        print(func.__name__, a, b, c)
    return wrapper

def slow_decorator(func):
    def wrapper(a, b, c):
        func(a, b, c)
        time.sleep(1)
    return wrapper        

def frequency(func):
    last = [time.perf_counter()]
    def decorator(a, b, c):
        if time.perf_counter() - last[0] < 10:
            raise RuntimeError('Please wait... ')
        last[0] = time.perf_counter()
        return func(a, b, c)
    return decorator

def quad_eq(a, b, c):
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


quad_eq_dec = time_decorator(quad_eq)
quad_eq_dec(1, 2, 3)

print()
quad_eq_dec = log_decorator(quad_eq)
quad_eq_dec(1, 2, 3)

print()
quad_eq_dec = slow_decorator(quad_eq)
quad_eq_dec = time_decorator(quad_eq_dec)
quad_eq_dec(1, 2, 3)

print()
quad_eq_dec = frequency(quad_eq)
time.sleep(15)
quad_eq_dec(1, 2, 3)

print()
quad_eq_dec(1, 2, 3)