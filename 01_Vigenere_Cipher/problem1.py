
letter = []

def preparePlainText():
	f = open("input.txt","r")
	string =""
	for i in f.read():
		string += i

	plainText = ''.join(filter(str.isalpha, string))
	return plainText

def prepareKey():
	k = open("key.txt","r")
	string = ""
	for i in k.read():
		string += i

	keyText = ''.join(filter(str.isalpha, string))
	keyTextLength = len(keyText)
	
	plainText = preparePlainText()
	plainTextLength = len(plainText)
	keyText = keyText * int(plainTextLength / keyTextLength) + keyText[0: plainTextLength % keyTextLength]
	return keyText

def code(x):
    keyText = prepareKey();
    if keyText[x].islower():
        return ord(keyText[x]) - 97
    else:
        return ord(keyText[x]) - 65 + 26

def encryption(plainText, keyText):

    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i].isupper():
            x = (ord(plainText[i]) - 65 + 26 + code(i)) % 52
            cipherText += letter[x]
        else:
            x = (ord(plainText[i]) - 97 + code(i)) % 52
            cipherText += letter[x]

    # print(cipherText)
    n = 5
    x = []
    for i in range(0, len(cipherText), n):
        x.append(cipherText[i:i+n])
    
    splittedCipher = ' '.join(str(ele) for ele in x)

    f = open("output.txt","w")
    f.write(splittedCipher)
    f.close()
    print("Encrypted Text :", splittedCipher)


def decryption(keyText):
    f = open("output.txt", "r")
    string = ""
    for i in f.read():
        string += i

    
    cipherText = ''.join(filter(str.isalpha, string))
    originalText = ""
    for i in range(len(cipherText)):
        if cipherText[i].isupper():
            x = (ord(cipherText[i]) - 65 + 26 - code(i)) % 52
            originalText += letter[x]
        else:
            x = (ord(cipherText[i]) - 97 - code(i)) % 52
            originalText += letter[x]

    print("After Decryption :",originalText)


for i in range(0,26):
    letter.append(chr(i + 97)) 

for i in range(26,52):
    letter.append(chr(i - 26 + 65)) 

plainText = preparePlainText()
keyText = prepareKey()
encryption(plainText, keyText)
decryption(keyText)
# print(letter)
