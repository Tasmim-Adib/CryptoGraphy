import array
import wave

#key scheduling Algorithm
def perform_KSA(key):
    length = len(key)
    temp = list(range(256)) #state vector
    j = 0
    for i in range(256):
        j = (j + temp[i] + key[i % length]) % 256
        temp[i], temp[j] = temp[j], temp[i]
    return temp #initial permutation vector

# Random number generator algorithm
def perform_PRGA(temp):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + temp[i]) % 256

        temp[i], temp[j] = temp[j], temp[i] #swap
        k = temp[(temp[i] + temp[j]) % 256]
        yield k
    
def keyStream(key, use_custom = False):

    key_from_KSA = perform_KSA(key)
    return perform_PRGA(key_from_KSA)

def perform_main(key, byteArray):
    key = [ord(c) for c in key]

    keystream = keyStream(key)

    result = []
    for i in byteArray:
        value = (i ^ next(keystream))
        result.append(value)
    return result

def encryption(key, byteArray):
    return perform_main(key,byteArray)

def decryption(key, cipher):
    result = perform_main(key, cipher)
    return array.array("B", result)
    
if __name__=="__main__":

    #read main.wav file
    key = "asdfghjklmnbvcxz";
    with wave.open('sample-9s.wav', 'rb') as wav_file:
        audio_params = wav_file.getparams() #get parameters
        #print(audio_params)
        frameData = wav_file.readframes(wav_file.getnframes())
        wav_file.close()

    cipherText = encryption(key,frameData)

    #save encrypted.wav
    with wave.open('encryptencrypteded.wav','wb') as wav_file:
        wav_file.setparams(audio_params)
        wav_file.writeframes(bytes(cipherText))
        wav_file.close()

    #save decrypted.wav
    decrypted_data = decryption("asdfghjklmnbvcxz",cipherText)
    with wave.open('decrypted.wav','wb') as wav_file:
        wav_file.setparams(audio_params)
        wav_file.writeframes(bytes(decrypted_data))
        wav_file.close()
    