# Author : Sagar Chandra Karmaker Babu
# Batch : 25
# Department of Computer Science and Engineering
# University of Dhaka

import sys
from BitVector import *
import DES




def getTextFromFile(fileName,isEncrypt):           
    f = open(fileName, 'r')
    t = f.read()
    f.close()
    ans = ""
    if not isEncrypt:
        # Decode bytes to string
        ans = BitVector(hexstring = t).get_text_from_bitvector()
    else:
        ans = t
    return ans

def getKey():
    f = open(sys.argv[2], 'r')
    tempString = f.read()
    f.close()
    return tempString
    



if len(sys.argv) != 4: 
    sys.exit("Needs three command-line arguments, one for  the encrypted file and the other for the  decrypted file and another for key ")

keyStr = getKey()
      
if sys.argv[1] == "message.txt":
    # get plain text
    text = getTextFromFile(sys.argv[1],True)
    # get BV of cipher text
    encryptedBV = DES.DES_function(text,keyStr,True)
    
    print("The encrypted Text is: ")
    print(encryptedBV.get_hex_string_from_bitvector())
    
    # save cipher Text
    with open(sys.argv[3], "w") as file:
        file.write(encryptedBV.get_hex_string_from_bitvector())

else:
    # get cipherText text
    text = getTextFromFile(sys.argv[1],False)
    # get BV of plain text
    decryptededBV = DES.DES_function(text,keyStr,False)
    
    print("The decrypted Text is: ")
    print(decryptededBV.get_text_from_bitvector())
    
    # save cipher Text
    with open(sys.argv[3], "w") as file:
        file.write(decryptededBV.get_text_from_bitvector().replace("\x00", ""))
    