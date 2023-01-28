MAX_KEY_LENGTH = 16     #we will not examine more than 16

def findRepeatedSequenceSpacing(message):
    message = message.upper()   #convert the message to upperCase
    seqSpacings = {}    #declaring dictionary for sequence spacing

    for seqLen in range(3,6):   #checking 3,4 and 5 length sequence
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]   #store the sequence

            for i in range(seqStart+seqLen, len(message) - seqLen):
                if message[i:i+seqLen] == seq:
                    if seq not in seqSpacings:      #if sequence matches and not in seqSpacing dictionary
                        seqSpacings[seq] = []       #create empty spacing for that sequence
                    seqSpacings[seq].append(i - seqStart)   #else add the length for that sequence
    
    #print(seqSpacings)
    return seqSpacings

def getFactors(num):        #calculating factors
    if num < 2:
        return []
    
    factors = []
    for i in range(2,MAX_KEY_LENGTH+1):
        if num % i == 0:
            factors.append(i)
            otherFactor = int(num/i)

            if otherFactor < MAX_KEY_LENGTH +1 and otherFactor != 1:
                factors.append(otherFactor)
    
    return list(set(factors))

def getItemAtIndexOne(x):
    return x[1]

def getMostCommonFactors(seqFactors):
    factorCounts = {}       #key is a factor and it's value is how often it occurs
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for i in factorList:        #iterate over all the factors
            if i not in factorCounts:
                factorCounts[i] = 0
            factorCounts[i] += 1    #count the factors

    #converting the factorCounts dictionary to a list
    factorsByCount = []
    for i in factorCounts:
        if i <= MAX_KEY_LENGTH:
            factorsByCount.append((i, factorCounts[i]))

    factorsByCount.sort(key = getItemAtIndexOne, reverse = True)
    #print(factorsByCount)
    return factorsByCount

def findKeyLength(message):
    repeatedSeqSpacings = findRepeatedSequenceSpacing(message)
    #print(repeatedSeqSpacings)
    seqFactors = {}
    for i in repeatedSeqSpacings:
        seqFactors[i] = []
        for j in repeatedSeqSpacings[i]:
            seqFactors[i].extend(getFactors(j))   #find every unique factor for every sequence
    
    factorsByCount = getMostCommonFactors(seqFactors)
    #print(factorsByCount)
    
    possibleKeyLength = []
    for i in factorsByCount:
        possibleKeyLength.append(i[0])
    
    return possibleKeyLength

