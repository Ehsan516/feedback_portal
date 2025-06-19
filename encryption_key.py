#for encryption

import nacl.secret
import nacl.utils
#nacl encrption api and rnadom byte generator

def generateKey():#helper funct to generate and save key
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)#32 byet random key
    with open("secret.key", "wb") as key_file:#opens the file named that
        key_file.write(key)#saves master key

if __name__ == "__main__":
    generateKey() #ran once for setup