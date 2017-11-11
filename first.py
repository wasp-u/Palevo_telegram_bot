import itertools

paintText = 'aba'
key = 'bbb'

rezult = [i for i in itertools.product(paintText,key)]

print(rezult)
ciphertext = ''.join([chr(r) for r in [ord(i) ^ ord(j) for i,j in rezult]])
print(ciphertext)
# ciphertext
# print(''.join([chr(i) for i in ciphertext]
# ))
t = [i for i in itertools.product(ciphertext,key)]
print(len(t))
text = ''.join([chr(i) for i in [ord(i) ^ ord(j) for i,j in t]])
print(text)