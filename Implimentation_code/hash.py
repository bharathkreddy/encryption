# implimented from : https://docs.python.org/3/library/hashlib.html

import hashlib

m = "This is the hash value message".encode()

SHA256 = hashlib.sha256()
SHA256.update(m)
d = SHA256.digest()

print(d)
print(SHA256.digest_size)

#lets modify just 1 bit of the message
def modify(m):
    l = list(m)
    print("original: ",l)
    l[0] = l[0]^1
    print("modified: ",l)
    return bytes(l)

m = modify(m)
print(m)
SHA256.update(m)
d = SHA256.digest()

print(d)




