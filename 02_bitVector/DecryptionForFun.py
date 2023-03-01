import sys
from BitVector import *

PassPhrase = "Hopes and dreams of a million years" 
BLOCKSIZE = 64 
numbytes = BLOCKSIZE // 8


# Reduce the passphrase to a bit array of size BLOCKSIZE:
bv_iv = BitVector(bitlist = [0]*BLOCKSIZE) 
for i in range(0,len(PassPhrase) // numbytes): 
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes] 
    bv_iv ^= BitVector( textstring = textstr )

# Create a bitvector from the ciphertext hex string:
FILEIN = open(sys.argv[1]) 
encrypted_bv = BitVector( hexstring = FILEIN.read() )

# Get key from user:
key = None
if sys.version_info[0] == 3:
    key = input("\nEnter key: ")
else:
    key = raw_input("\nEnter key: ") 
key = key.strip()

# Reduce the key to a bit array of size BLOCKSIZE:
key_bv = BitVector(bitlist = [0]*BLOCKSIZE) 
for i in range(0,len(key) // numbytes): 
    keyblock = key[i*numbytes:(i+1)*numbytes]
    key_bv ^= BitVector( textstring = keyblock )

print(key_bv)
# Create a bitvector for storing the decrypted plaintext bit array:
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

#write to the output file
FILEOUT = open(sys.argv[2], 'w') 
FILEOUT.write(outputText)
FILEOUT.close()