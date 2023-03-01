import FindKeyLength
import frequencyAnalysis
import attack

def prepareCipherText():
    f = open("output.txt","r")
    string = ""
    for i in f.read():
        string += i
    message = "".join(string.split())
    return message

def main():
    message = prepareCipherText()

    #repeatedSequence = FindKeyLength.findPattern(message)
    #print(repeatedSequence)

    #possibleKeyLength = FindKeyLength.predictKeyLength(message)
    #print(possibleKeyLength)
    attack.decryptVigenereCipher(message)
    

if __name__ == '__main__':
    main()