# RSA (Rivest–Shamir–Adleman) 1977

Proposed 1 year after D-H key exchange method. The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". There are no published methods to defeat the system if a large enough key is used. 

RSA is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. More often, RSA is used to transmit shared keys for symmetric-key cryptography, which are then used for bulk encryption–decryption.

Comes with 1024, 2048, 3072 and  4096 Key sizes. RSA beyond 260 has [not been broken yet](https://en.wikipedia.org/wiki/RSA_Factoring_Challenge)

### STEPS IN RSA
1. Key Generation
    - p,q <- Primes.
    - n = p * q <- modulus (calculating p & q given n is an np complete problem.)
    - e < - exponent
    - d <- modular multiplicative inverse to e

2. Public Key
    - (n,e)
    - message m is encrypted to cipher c as : c = m^e mod n

3. Private Key
    - d
    - decript cipher c to message m as : m = c^d mod n

[Native from Scratch Implementation of RSA](/Implimentation_code/rsa.py)
[GnuPg implementation of RSA](/Implimentation_code/Asymmetric_key_GnuPg.md)
[OpenSSL implementation of RSA](/Implimentation_code/Asymmetric_key_openssl.md)





