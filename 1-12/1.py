def listEncode(list):
    '''Encode all elements of passed list'''
    for i in range(len(list)):
        list[i] = list[i].encode()

def listDecode(list):
    '''Decode all elements of passed list'''
    for i in range(len(list)):
        list[i] = list[i].decode()

list=['the','list',
    'of', 'string']
print("---Orig list:")
for s in list:
    print(s)
listEncode(list)
print("---Encoded list:")
for s in list:
    print(s)
listDecode(list)
print("---Decoded list:")
for s in list:
    print(s)