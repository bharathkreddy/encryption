# Steps implemented from : https://en.wikipedia.org/wiki/RSA_(cryptosystem)

import math
import random


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

print("Generated Primes:", p, q)

# STEP 2: Compute n = p*q. n is released as part of public key and len n is the key lenght.
n = p * q
print("Modulus n:", n)

# STEP 3: Compute lambda(n) = lcm(p-1. q-1) keep this secret. Use lcm(a, b) = |ab|/gcd(a, b) 
def lcm(a,b):
    return a*b//math.gcd(a, b)  #returns the integer part and ignore the decimal part, this is needed to calculate public exponent.

lambda_n = lcm(p-1,q-1)
print("λ(n):", lambda_n)

# STEP 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime. This is the public exponent
def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False
    
e = get_e(lambda_n)
print("Public Exponent: ", e)

# STEP 5: Solve for d in the equation d.e ≡ 1 (mod λ(n))
def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

d = get_d(e, lambda_n)
print("Secret Exponent: ",d)

# Done with key generation
print("Public Key (e,n):", e,n)
print("Private Key (d):", d)


# Bob trying to send a message to Alice. Bob has Alices public key (e,n)
m = 117
c =  (m**e) % n
print("cipher text:",c)

# Alice decrypting the message with her private key (d)
m = (c**d) % n
print("message:",m)


# This is EVE
print("Eve sees the following:")
print("public key (e, n):", e, n)
print("encrypted cipher (c):", c)

def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p

E_p,E_q = factor(n)
print("Eve'sfactors are :",p, q)

E_lambda_n = lcm(E_p-1,E_q-1)
print("Eves λ(n):", E_lambda_n)

E_e = get_e(E_lambda_n)
print("Eves Public Exponent: ", E_e)

E_d = get_d(E_e, E_lambda_n)
print("Eves Secret Exponent: ",E_d)

E_m = (c**E_d) % n
print("Eves decrypted message:",E_m)

## This is BOB not being careful while sending messages
## NEVER ENCRYPT LETTER BY LETTER - defeting entire purpose of block ciphers !!
print("This is Bob being careless")
message = "Alice is awsome, Eve is not"
for m_c in message:
    c = (ord(m_c)**e) % n  # All "e" are ecrypted the same !!
    print(m_c," ",end="")
    print(c," ",end='')




print()