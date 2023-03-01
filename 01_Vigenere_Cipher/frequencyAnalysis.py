
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# 1. Counting the letters in the string
# 2. Creating a dictionary of frequency counts and letter lists
# 3. Sorting the letter lists in reverse ETAOIN order
# 4. Converting this data to a list of tuples
# 5. Converting the list into the final string to return from the function getFrequencyOrder()


# 1. Counting the letters in the string
def getLetterCount(message):

    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                    'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for i in message.upper():
        if i in LETTERS:
            letterCount[i] += 1
    return letterCount

def getItemAtIndexZero(item):
    return item[0]

# 2. Creating a dictionary of frequency counts and letter lists
def getFrequencyOrder(message):
    letterCount = getLetterCount(message)   #find letter frequency
    #return letterCount

    # 3. merge letter with same frequency
    freqToLetter = {}
    for i in LETTERS:
        if letterCount[i] not in freqToLetter:
            freqToLetter[letterCount[i]] = [i]
        else:
            freqToLetter[letterCount[i]].append(i)
    
    #return freqToLetter

    # 4. put the letters in ETAOIN order and make them string
    for i in freqToLetter:
        freqToLetter[i].sort(key = ETAOIN.find, reverse = True)
        freqToLetter[i] = ''.join(freqToLetter[i])

    #return freqToLetter

    # 5. convert the dictionary to list
    freqPair = list(freqToLetter.items())
    freqPair.sort(key = getItemAtIndexZero, reverse = True)

    #return freqPair

    #letters are ordered by frequency so extract the final string
    freqOrder = []
    for i in freqPair:
        freqOrder.append(i[1])
    
    return ''.join(freqOrder)

#calculating the frequency match score
def findMatchingScore(message):
    matchScore = 0
    freqOrder = getFrequencyOrder(message)
    #find match in most common letters
    for i in ETAOIN[:6]:
        if i in freqOrder[:6]:
            matchScore += 1

    #find match in least common letters
    for i in ETAOIN[-6:]:
        if i in freqOrder[-6:]:
            matchScore += 1
    
    return matchScore