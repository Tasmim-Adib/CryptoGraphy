from BitVector import *
import itertools as it


def readFile(filename:str):
    value = []
    with open(filename, "r") as f:
        for line in f:
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            value.append(list(map(int, line.split(","))))
            # print(line.split(","))
    # print(value)
    return value

validChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!-()., '
punctuations = ['.', ',', ' ', '(', ')', '-', '!', '?']

def findInList(words:list, value:str):
    try:
        return words.index(value)
    except ValueError:
        return -1


def cryptoanalysis(prevcipherletter, cipherLetters):
    candidate_char = []
    pad = []
    validity = 0
    for i in range(256):
        for j in range(len(cipherLetters)):
            moddedVal = ((prevcipherletter[j]) + i)%256
            mod_bv = BitVector(size=8, intVal= moddedVal)
            # print(cipherLetters[j])
            cipher_bv = BitVector(size= 8, intVal= cipherLetters[j])
            xor_val_bv = mod_bv ^ cipher_bv
            xor_val = xor_val_bv.get_text_from_bitvector()
            if validChar.find(xor_val) != -1:
                validity += 1
        
        if (validity) >= 10:
            pad.append(i)
            candidate_char.append(xor_val)
        validity = 0

    return candidate_char, pad


def findMessage(idxWiseVal):

    words = []
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            words.append(line.strip('\n')) #line

    candidate_chars = []
    candidate_pads = []

    candidate_char, pad = cryptoanalysis([0]*10, idxWiseVal[0])
    candidate_chars.append(candidate_char)
    candidate_pads.append(pad)
    

    for i in range(1, len(idxWiseVal)):
        candidate_char, pad = cryptoanalysis(idxWiseVal[i-1], idxWiseVal[i])
        candidate_chars.append(candidate_char)
        candidate_pads.append(pad)

    print(candidate_chars, candidate_pads)
        
    # print(len(words), len(punctuations))

    total_permutation = []
    idx_for_punctuations = []
    val = 1
    for i in range(len(candidate_chars)):
        if all(elem in punctuations for elem in candidate_chars[i]):
            total_permutation.append(val)
            idx_for_punctuations.append(i)
            val = 1
        else:
            val *= (len(candidate_chars[i]))
        if i == len(candidate_chars)-1:
            total_permutation.append(val)
 
    msg = []
    prev = 0
    idx_for_punctuations.append(60)
    print(total_permutation, idx_for_punctuations)

    for j in range(len(idx_for_punctuations)):
        ax = []
        for i in range(total_permutation[j]):
            s = ''.join(list(it.product(*candidate_chars[prev:idx_for_punctuations[j]]))[i])
            if findInList(words=words, value = s) != -1:
                ax.append(s)
        msg.append(ax)
        prev = idx_for_punctuations[j]+1

    return msg
    
def decrypt(message, CipherText):

    prevcipherletter = 0
    probablePad =''
    for i in range(len(CipherText)):
        message_bv = BitVector(size = 8, intVal = ord(message[i]))
        cipher_bv = BitVector(size = 8, intVal = (CipherText[i]))
        # moddedVal = (ord(message[i])+ (prevcipherletter))%256
        unmodded_val_bv = message_bv ^ cipher_bv
        unmodded_val = ord(unmodded_val_bv.get_text_from_bitvector())
        probable_pad = (unmodded_val - prevcipherletter) %256
        probablePad += chr(probable_pad)
        prevcipherletter = CipherText[i]

    return probablePad



def main():
    
    idxWiseVal = []
    
    ciphertexts = readFile("Ciphertext_Assignment_3.txt")

    for i in range(len(ciphertexts[0])):
        val = []
        for j in range(len(ciphertexts)):
            a = (j+0)%10
            val.append(ciphertexts[a][i])
        idxWiseVal.append(val)

    msg10 = findMessage(idxWiseVal)

    val = 1
    for i in range(len(msg10)):
        val *= len( msg10[i])

    print(val)

    for i in range(len(msg10)):
        print(msg10[i])

    messages = []
    for i in range(val):
        messages.append(' '.join(list(it.product(*msg10[:]))[i]))
    print(messages)
    

    #print(decrypt(messages[15], ciphertexts[9]))
    
    
    

if __name__ == '__main__':
    main()