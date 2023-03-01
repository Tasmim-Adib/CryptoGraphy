
from BitVector import *

BLOCKSIZE = 8
message = "OneTimePad"
key = "asdfghjkli"

def encryption():
    previous_cipher = str(0)
    msg_encrypted_bv = BitVector(size = 0)
    
    for i in range(len(message)):
        x = (ord(key[i]) + ord(previous_cipher)) % 256
        ext_bv = BitVector(size = 8, intVal = x)
        text_bv = BitVector(size = 8, intVal = ord(message[i]))

        # print(BitVector(intVal = x))
        # print(BitVector(textstring = message[i]))

        cipherBlock = ext_bv ^ text_bv
        # print(cipherBlock)

        previous_cipher = cipherBlock.get_text_from_bitvector()
        msg_encrypted_bv += cipherBlock
    return msg_encrypted_bv.get_text_from_bitvector()

def decryption(cipherText):
    previous_cipher = str(0)
    msg_decrypted_bv = BitVector(size = 0)
    for i in range(len(key)):

        x = (ord(key[i]) + ord(previous_cipher)) % 256
        ext_bv = BitVector(size = 8, intVal = x)
        text_bv = BitVector(size = 8, intVal = ord(cipherText[i]))

        cipherBlock = ext_bv ^ text_bv   
        previous_cipher = cipherText[i]

        msg_decrypted_bv += cipherBlock
        
    return msg_decrypted_bv.get_text_from_bitvector()

def main():
    encryptedHex = encryption()
    print('Encrypted Text :',encryptedHex)
    decrypted_message = decryption(encryptedHex)
    print('Decrypted Text :',decrypted_message)

if __name__=="__main__":
    main()