from BitVector import *
import S_Box
import RoundKey

BLOCKSIZE = 64


expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]



initial_permutation_matrix = [  
        57, 49, 41, 33, 25, 17,  9,  1,
        59, 51, 43, 35, 27, 19, 11,  3,
        61, 53, 45, 37, 29, 21, 13,  5,
        63, 55, 47, 39, 31, 23, 15,  7,
        56, 48, 40, 32, 24, 16,  8,  0,
        58, 50, 42, 34, 26, 18, 10,  2,
        60, 52, 44, 36, 28, 20, 12,  4,
        62, 54, 46, 38, 30, 22, 14,  6  ]

initial_reverse_permutation_matrix = [  
                39,  7, 47, 15, 55, 23, 63, 31,
                38,  6, 46, 14, 54, 22, 62, 30,
                37,  5, 45, 13, 53, 21, 61, 29,
                36,  4, 44, 12, 52, 20, 60, 28,
                35,  3, 43, 11, 51, 19, 59, 27,
                34,  2, 42, 10, 50, 18, 58, 26,
                33,  1, 41,  9, 49, 17, 57, 25,
                32,  0, 40,  8, 48, 16, 56, 24  ]

p_box = [   15,  6, 19, 20, 28, 11, 27, 16,
             0, 14, 22, 25,  4, 17, 30,  9,
             1,  7, 23, 13, 31, 26,  2,  8,
            18, 12, 29,  5, 21, 10,  3, 24  ]




def DES_function(plainText,key,isEncrypt):
    
    
    finalBV = BitVector(size = 0)
    # get round keys
    round_keys = RoundKey.generate_round_keys(key)
    # if decryption then reverse the round keys
    if not isEncrypt:
        round_keys.reverse()
    
    # get array of 8 charachter substring in order to get 64 bit plain text
    substrings = [plainText[i:i+8] for i in range(0, len(plainText), 8)]
  
    for subString in substrings:
        
        bv_read = BitVector(textstring = subString)
        # if length of bv is less than 64 then concat 0s
        if len(bv_read) < BLOCKSIZE: 
                bv_read += BitVector(size = (BLOCKSIZE - len(bv_read))) 
        
        # permute the 64 bit text and divide it in two equal parts
        bv_read = bv_read.permute(initial_permutation_matrix)
        [LE, RE] = bv_read.divide_into_two()

        for x in range(0,16):
            
            currentRoundKey = round_keys[x]
           
            newRE = RE.permute( expansion_permutation )
            newRE = newRE^currentRoundKey
            newRE = S_Box.substitute(newRE)
            
            newRE = newRE.permute(p_box)
            finalRE = newRE^LE
            LE = RE
            RE = finalRE
        
        tempBV = RE + LE
        
        tempBV = tempBV.permute(initial_reverse_permutation_matrix)
        finalBV += tempBV
        
    return finalBV        

