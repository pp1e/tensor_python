key=input('Input key: ')
key=list(key)

with open('text.txt','r') as inputFile:
    text=inputFile.read()
    text=list(text)
    for i in range(len(text)):
        text[i]=ord(text[i]) ^ ord(key[i % len(key)])

encodedText=''
for t in text:
    encodedText+=chr(t)
with open('Encoded.txt','w') as outputFile:
    outputFile.write(encodedText)   


for i in range(len(text)):
    text[i]=chr(text[i] ^ ord(key[i % len(key)]))

with open('Decoded.txt','w') as outputFile:
    outputFile.write(''.join(text))   
