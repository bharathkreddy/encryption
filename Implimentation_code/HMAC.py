import hashlib

#ALICE and BOB share a key
secret_key = "secret key".encode()

# ALICE computes MAC
m = "Hey Bob. You are awesome".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print(m, hmac)

# BOB receives the message
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
bobs_hmac = sha256.digest()
print(m,bobs_hmac)