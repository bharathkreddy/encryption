"""
Suppose Alice uses Bob's public key to send him an encrypted message. In the message, she can claim to be Alice, but Bob has no way of verifying that the message 
was from Alice, since anyone can use Bob's public key to send him encrypted messages. In order to verify the origin of a message, RSA can also be used to 
sign a message.

Suppose Alice wishes to send a signed message to Bob. She can use her own private key to do so. She produces a hash value of the message, 
raises it to the power of d (modulo n) (as she does when decrypting a message), and attaches it as a "signature" to the message. 
When Bob receives the signed message, he uses the same hash algorithm in conjunction with Alice's public key. He raises the signature to the power of e (modulo n)
 (as he does when encrypting a message), and compares the resulting hash value with the message's hash value. If the two agree, he knows that the author 
 of the message was in possession of Alice's private key and that the message has not been tampered with since being sent.
"""
# Step 1: Get generate the public key and Private key (we can do the same steps as we did in RSA file)
import math
import random

## LINE 16 - LINE 72 generates the RSA keys.
print()
print("Step 1: generating public and private RSA keys")
def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


# Key generation done by ALICE.
# STEP 1: Generate two distinct prime numbers and keep them secret
size = 1000
p = get_prime(size)
q = get_prime(size)
# STEP 2: Compute n = p*q. n is released as part of public key and len n is the key lenght.
n = p * q
# STEP 3: Compute lambda(n) = lcm(p-1. q-1) keep this secret. Use lcm(a, b) = |ab|/gcd(a, b) 
def lcm(a,b):
    return a*b//math.gcd(a, b)  #returns the integer part and ignore the decimal part, this is needed to calculate public exponent.
lambda_n = lcm(p-1,q-1)
# STEP 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime. This is the public exponent
def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False  
e = get_e(lambda_n)
# STEP 5: Solve for d in the equation d.e ≡ 1 (mod λ(n))
def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

d = get_d(e, lambda_n)

# These are ALICE's Keys
print("Public Key (e,n):", e,n)
print("Private Key (d):", d)

# This is the message that Alice wants to send to Bob
message = "Bob you are awesome".encode()
print()
print("Step 2: Generating SHA-256 digest of message")

import hashlib
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n # we do % n because the digest needs to be encrypted and for our toy examples value of mod n is small and would not be able to encrypt the entire digest, so we reduce the digetst to a small number, this is just fo this example and should not be done in real life. 
print(h) 

print()
print("Step 3: Alice decrypting the hash with her private key d")
sign = (h**d) % n
print(sign)

# BOB verifies the signature
print()
print("Step 4: Alice Sends the message with signature to bob")

print()
print("Step 5: Bob encrypting the sign with Alices public key e")

bob_hash = (sign**e) % n
print("bobs hash from signature: ",bob_hash)

print()
print("Step 6: Bob calculates the hash from message using same SHA256 algo")
sha256 = hashlib.sha256()
sha256.update(message)
b_h = sha256.digest()
b_h = int.from_bytes(b_h, "big") % n 
print("bobs calculated hash of message: ",b_h)
