key=input('Input key: ')
key=list(key)

with open('text.txt', 'r') as input_file:
    text=input_file.read()
    text=list(text)
    for i in range(len(text)):
        text[i] = ord(text[i]) ^ ord(key[i % len(key)])

encoded_text = ''
for t in text:
    encoded_text += chr(t)
with open('Encoded.txt', 'w') as output_file:
    output_file.write(encoded_text)   


for i in range(len(text)):
    text[i] = chr(text[i] ^ ord(key[i % len(key)]))

with open('Decoded.txt', 'w') as output_file:
    output_file.write(''.join(text))   
