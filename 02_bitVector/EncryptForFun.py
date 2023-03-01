
import sys
from BitVector import *

PassPhrase = "Hopes and dreams of a million years"

BLOCKSIZE = 64 
numbytes = BLOCKSIZE // 8

#print(numbytes)
#reduce the PassPhrase to a bit array of size BLOCKSIZE
bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)
#print(bv_iv)
for i in range(0, len(PassPhrase) // numbytes):
    textstr = PassPhrase[i * numbytes : (i+1)*numbytes]
    #print(textstr)
    bv_iv ^= BitVector(textstring = textstr)
    # print(bv_iv)
#print(bv_iv)
# Get key from user:
key = None
if sys.version_info[0] == 3:    #checking version
    key = input("\nEnter key: ")    #if it is python3
else:
    key = raw_input("\nEnter key: ")    #if it is python2

key = key.strip()

# Reduce the key to a bit array of size BLOCKSIZE:
key_bv = BitVector(bitlist = [0]*BLOCKSIZE) #(N)
#print(key)
for i in range(0,len(key) // numbytes): #(O)
    keyblock = key[i*numbytes:(i+1)*numbytes] #(P)
    key_bv ^= BitVector( textstring = keyblock )

#creating a bitvector for storing ciphertext bit array
msg_encrypted_bv = BitVector(size = 0)

#carray out differential XORing of bit blocks and encryption
previous_block = bv_iv 
bv = BitVector( filename = sys.argv[1] )
while (bv.more_to_read): 
    bv_read = bv.read_bits_from_file(BLOCKSIZE)

    if len(bv_read) < BLOCKSIZE: 
        bv_read += BitVector(size = (BLOCKSIZE - len(bv_read))) 
    bv_read ^= key_bv 
    bv_read ^= previous_block 
    previous_block = bv_read.deep_copy() 
    msg_encrypted_bv += bv_read
    #print(msg_encrypted_bv)


# Convert the encrypted bitvector into a hex string:
outputhex = msg_encrypted_bv.get_hex_string_from_bitvector() 

# Write ciphertext bitvector to the output file:
FILEOUT = open(sys.argv[2], 'w') 
FILEOUT.write(outputhex) 
FILEOUT.close()