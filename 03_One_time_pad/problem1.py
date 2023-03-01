import dawg
from BitVector import *

def encryptedHex(hex_value):
    encryted_bv = BitVector(hexstring = hex_value)
    return encryted_bv

def findInPredictedWordList(predictedWord:list, item:str):
    try:
        return predictedWord.index(item)
    except ValueError:
        return -1

if __name__=="__main__":
    words = open('/usr/share/dict/words', 'r').read().splitlines()
    predictedWord = []
    for i in words:
        if len(i) == 8:
            predictedWord.append(i)
    
    cipher1 = "e93ae9c5fc7355d5"
    cipher2 = "f43afec7e1684adf"
    message1_bv = encryptedHex(cipher1)
    message2_bv = encryptedHex(cipher2)
    message_xor = message1_bv ^ message2_bv
    
    for i in predictedWord:
        i_bv = BitVector(textstring = i)
        #print(i_bv)
        message_bv_decrypted = i_bv ^ message_xor
        decrypted_message = message_bv_decrypted.get_text_from_bitvector()
        x = findInPredictedWordList(predictedWord = predictedWord, item = decrypted_message)
        if(x != -1):
            break
    print(i)
    print(decrypted_message)
