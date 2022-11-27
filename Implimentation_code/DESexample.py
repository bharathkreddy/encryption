from pyDes import *
message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key=key,mode=ECB, IV=iv, pad=None,padmode=PAD_PKCS5) # uses Electronic code book mode

cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher[0:8])
print("Encrypted:", cipher[8:16])  #given same paintext, the cipher also stays same.
print("Encrypted:", cipher[16:])

message = k.decrypt(cipher)
print("Decrypted:", message)



k = des(key=key,mode=CBC, IV=iv, pad=None,padmode=PAD_PKCS5) # uses Cipher Block Chaining method

cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher[0:8])
print("Encrypted:", cipher[8:16]) #given same paintext, now the cipher changes.
print("Encrypted:", cipher[16:])

message = k.decrypt(cipher)
print("Decrypted:", message)


# LETS TRY TAMPERING THIS CIPHER LIKE WE DID FOR STREAM CIPHER
# ALICE  sends this to bank
message = "123456789101112131415161718192021222324252627282930"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key=key,mode=ECB, IV=iv, pad=None,padmode=PAD_PKCS5) 

cipher = k.encrypt(message)
print("Alice using ECB for encryption")
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)


# This is bob tampering the cipher.
def modification(cipher): 
    mod = [0] * len(cipher)  #creates a zero array of same legth as cipher, now we can modify this array at some places to change the cipher
    mod[13] = 1  # Change one bit and see what happens , if we change 0-7 ( any first 8 bits) the first block gets destroyed, after 8-16 the second block gets destryed
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))]) # XOR with cipher and we have modified the cipher. see what the bank sees now.


cipher = modification(cipher)
print("new cipher:",cipher)


# This is BANK deconding the message
message = k.decrypt(cipher)
print("Decrypted:",message) # we have modified only block, so in output only a part of message gets scrambled, changing a single item in block causes entire block to be destroyed.

# Lets try the same example in CBC mode. 
# ALICE  sends this to bank
message = "Send bob:    10$, and send 40$ to the bricklyer"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key=key,mode=CBC, IV=iv, pad=None,padmode=PAD_PKCS5) # MODE NOW CHANGED TO CBC
cipher = k.encrypt(message)
print("Alice using CBC for encryption")
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)


# This is bob tampering the cipher.
def modification(cipher): 
    mod = [0] * len(cipher)  
    mod[5] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))]) 

cipher = modification(cipher)
print("new cipher:",cipher)


# This is BANK deconding the message
message = k.decrypt(cipher)
print("Decrypted:",message) # we have modified only block, the tampered block gets destroyed and a few bits in next block.