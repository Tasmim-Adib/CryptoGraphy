
import sys
from BitVector import *

BLOCKSIZE = 16
PassPhrase = "Hopes and dreams of a million years"
numbytes = BLOCKSIZE // 8

def makeInitialVector():
    bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)

    for i in range(0, len(PassPhrase) // numbytes):
        textstr = PassPhrase[i*numbytes : (i+1)*numbytes]
        bv_iv ^= BitVector(textstring = textstr)
    
    return bv_iv

def getEncryptedText():
    FILEIN = open(sys.argv[1]) 
    encrypted_bv = BitVector( hexstring = FILEIN.read() )
    return encrypted_bv

def attack(key,bv_iv,encrypted_bv):

    key_bv = BitVector(bitlist = [0]*BLOCKSIZE) 
    for i in range(0,len(key) // numbytes): 
        keyblock = key[i*numbytes:(i+1)*numbytes]
        key_bv ^= BitVector( textstring = keyblock )
    
    #print(key_bv)
    msg_decrypted_bv = BitVector( size = 0 )

    #carry out differential XORing
    previous_decrypted_block = bv_iv
    for i in range(0, len(encrypted_bv) // BLOCKSIZE):
        bv = encrypted_bv[i * BLOCKSIZE : (i+1)*BLOCKSIZE]
        temp = bv.deep_copy()
        bv ^= previous_decrypted_block
        previous_decrypted_block = temp
        bv ^= key_bv
        msg_decrypted_bv += bv

    #extract plaintext
    outputText = msg_decrypted_bv.get_text_from_bitvector()
    return outputText

def main():
    bv_iv = makeInitialVector()
    encrypted_bv = getEncryptedText()
    # print(bv_iv)
    # print(encrypted_bv)
    key = ""
    # outputText = attack('st')
    # print(outputText)
    # for i in range(0, len(letters)):
    #     for j in range(0,len(letters)):
    #         key = letters[i] + letters[j]
    #         #print(key)
    #         outputText = attack(key)
    #         print('Key is : '+key)
    #         print('Output Text is : '+outputText)
    #         print("If decryption is successful the write done !!")
    #         x = input()

    print('-----Kindly wait a few moment-----')
    for i in range(0,256):
        for j in range(0,256):
            key = chr(i) + chr(j)
            outputText = attack(key,bv_iv,encrypted_bv)
            if outputText.find('Douglas Adams') != -1:
                print('Key : '+key)
                print("Original Message : "+outputText)
                break
    
    # print('-----Kindly wait a few moment-----')
    # for i in range(97,123):
    #     for j in range(97,123):
    #         key = chr(i) + chr(j)
    #         outputText = attack(key,bv_iv,encrypted_bv)
    #         if outputText.find('Douglas Adams') != -1:
    #             print('Key : '+key)
    #             print("Original Message : "+outputText)
    #             # break

if __name__=="__main__":
    main()