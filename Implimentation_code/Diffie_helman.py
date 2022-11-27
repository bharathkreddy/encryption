import math
import random

# Implementing a Random Prime Generator.
def is_prime(p):
    for i in range(2, math.isqrt(p)+1):   # isqrt returns the integer part of sqrt
        if p % i == 0:
            return False
        else:
            return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size) # while randint returns the range including endpoint, randrange exclues the endpoints.
        if is_prime(p):
            return p

# Implementing a generator
def is_generator(g, p):
    for i in range(1, p-1):
        if (g**1) % p == 1:
            return False
    return True

def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return(g)

p = get_prime(10000)
g = get_generator(p)
print(g,p)

# Implementing Diffie-Helman Exchange

# Alice
a = random. randrange(0, p)
g_a = (g**a) % p
#ALICE sends this to Bob
print("Alice sends to Bob: ",g_a)

# Bob
b = random. randrange(0, p)
g_b = (g**b) % p
#Bob sends this to ALICE
print("Bob sends to ALICE: ",g_b)

# ALICE calculates the shared key
g_ab = (g_b**a) % p
print("Alice's Key: ", g_ab)

# BOB calculates the shared key
g_ba = (g_a**b) % p
print("Bob's Key: ", g_ba)

