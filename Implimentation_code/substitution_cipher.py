import random

def generate_key():
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cletters = list(letters)
    key = {}
    for i in letters:
        key[i]=cletters.pop(random.randint(0,len(cletters)-1))
    return key

def encrypt(plain_text,key):
    cipher_text = []
    for i in plain_text:
        if i in key:
            cipher_text.append(key[i])
        else:
            cipher_text.append(i)
    return ''.join(cipher_text)

def decrypt(cipher_text,key):
    dkey={}
    for i in key:
        dkey[key[i]]=i  #we are just creating a dict with values as keys from the encryption key dict
    plain_text = encrypt(cipher_text,dkey)
    return plain_text

plain_text = "YOU ARE AWSOME"
key = generate_key()
cipher_text = encrypt(plain_text,key)
print(cipher_text)

decrypted_text = decrypt(cipher_text,key)
print(decrypted_text)


