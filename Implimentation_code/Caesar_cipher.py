# Caesar Cipher or shift cipher is one of the simplest and most widely known encryption techniques. 
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

def generate_key(n):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key ={}
    cnt = 0
    for i in letters:
        key[i]=letters[(cnt+n) % len(letters)] # after Z the letters have to fold over to start
        cnt += 1
    return key

def encrypt(message,n):
    key = generate_key(n)
    cipher_text = []
    for i in message:
        if i in key:  # to accomodate spaces or special chars, these should be left as is.
            cipher_text.append(key[i])
        else:
            cipher_text.append(i)
    return ''.join(cipher_text) # convert the list to a string.

def decrypt(cipher,n):
    inv_key = generate_key(n)
    key = {inv_key[x]:x for x in inv_key}
    plain_text=[]
    for i in cipher:
        if i in key:
            plain_text.append(key[i])
        else:
            plain_text.append(i)
    return ''.join(plain_text)

message = "YOU ARE TERRIBLE"

cipher = encrypt(message,3)
print("Message : {}".format(message))
print("Cipher Text : {}".format(cipher))

cipher = "BRX DUH DZHVRPH"

plain_text = decrypt(cipher,3)
print("Cipher Text : {}".format(cipher))
print("Plain Text : {}".format(plain_text))