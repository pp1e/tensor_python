import random

a=[]
b=[]
for i in range(random.randint(1, 10)):
    a.append(random.randint(-1000, 1000))
for i in range(random.randint(1, 10)):
    b.append(random.randint(-1000, 1000))

print(a)
print(b)
a=set(a)
b=set(b)

print('A⋂B' + str(a.intersection(b)))
print('A\(A⋂B)' + str(a.difference(b)))
print('B\(A⋂B)' + str(b.difference(a)))
print('(AUB)\(A⋂B)' + str(a.symmetric_difference(b).union(b.symmetric_difference(a))))
