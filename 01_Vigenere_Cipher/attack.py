
import frequencyAnalysis
import FindKeyLength
import itertools

letter = []
NUM_MOST_FREQ_LETTER = 5

# get nth letter and make string
def getNthLetter(nth, keyLength, message):
    i = nth - 1
    letters = []

    while i < len(message):
        letters.append(message[i])
        i += keyLength
    
    return ''.join(letters)

def code(x):
    if x.islower():
        return ord(x) - 97
    else:
        return ord(x) - 65 + 26

def getItemAtIndexOne(item):
    return item[1]

def decrypt(key, cipherText):
    keyTextLength = len(key)
    cipherTextLength = len(cipherText)
    key = key * int(cipherTextLength / keyTextLength) + key[0: cipherTextLength % keyTextLength]
	
    originalText = ""

    for i in range(0,26):
        letter.append(chr(i + 97)) 
    for i in range(26,52):
        letter.append(chr(i + 65-26))

    for i in range(cipherTextLength):
        if cipherText[i].isupper():
            x = (ord(cipherText[i]) - 65 + 26 - code(key[i])) % 52
            originalText += letter[x]
        else:
            x = (ord(cipherText[i]) - 97 - code(key[i])) % 52
            originalText += letter[x]

    return originalText


def attemptDecrypt(cipherText, mostPossibleKeyLength):
    cipherTextUp = cipherText.upper()
    
    allFreqScores = []
    for i in range(1, mostPossibleKeyLength + 1):
        nthLetters = getNthLetter(i, mostPossibleKeyLength, cipherTextUp)
        freqScores = []
        #print('%sth letter sequence : ' %(i), nthLetters)
        #decrypt nth letter and store the letter with most frequency
        for possibleKey in frequencyAnalysis.LETTERS:
            decryptedText = decrypt(possibleKey, nthLetters)

            keyAndFreqMatchTuple = (possibleKey, frequencyAnalysis.findMatchingScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        
        freqScores.sort(key = getItemAtIndexOne, reverse = True)
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTER])

    for i in range(len(allFreqScores)):
        print('Possible Keyletter for pattern %s: ' %(i+1), end = '')

        for j in allFreqScores[i]:
            print('%s ' %(j[0]), end = '')
        print()
    
    for index in itertools.product(range(NUM_MOST_FREQ_LETTER), repeat = mostPossibleKeyLength):
        possibleKey = ''
        for i in range(mostPossibleKeyLength):
            possibleKey += allFreqScores[i][index[i]][0]

            if len(possibleKey) != mostPossibleKeyLength:
                continue

            print('Attempting with the key: %s ' %(possibleKey))
            decryptedText = decrypt(possibleKey,cipherTextUp)

            origText = []
            for i in range(len(cipherText)):
                if cipherText[i].isupper():
                    origText.append(decryptedText[i].upper())
                else:
                    origText.append(decryptedText[i].lower())

            decryptedText = ''.join(origText)
            print('Possible text using key : %s ' %(possibleKey))
            print(decryptedText[:150])
            print()
            print('Write Hurray if done or press enter to continue..')
            response = input('> ')

            if response.strip() == 'Hurray':
                return decryptedText
    
    return None


def decryptVigenereCipher(cipherText):
    possibleKeyLength = FindKeyLength.predictKeyLength(cipherText)
      
    keyLength = ''
    for i in possibleKeyLength:
        keyLength += '%s ' %(i)
    print('The most probable key lengths are sorted in order : ' + keyLength + '\n')

    originalMessage = None
    for i in possibleKeyLength:
        print('Decrypt with key length %s (%s possible keys)...'% (i, NUM_MOST_FREQ_LETTER ** i))
        originalMessage = attemptDecrypt(cipherText, i)
            
        if originalMessage != None:
            break
        
    return originalMessage

