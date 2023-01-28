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
    attack.decryptVigenere(message)
    

if __name__ == '__main__':
    main()