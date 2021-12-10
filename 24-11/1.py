list1=[
    2, 5, 4, 7, 8,
    12, 76, 45, 9,
    0, -2, 64, -40
    ]

for i in range(0, len(list1)):
    for j in range(1, len(list1)-i):
        if (list1[j-1] > list1[j]):
            list1[j-1], list1[j] = list1[j], list1[j-1]

print(list1)