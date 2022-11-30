# Encryption 

This writeup gives 
1. An overview of encryption, two broad types of keys (symmetric and asymmetric) & differences. Working examples with multiple libraries.
2. Overview of SSH, TLS and Key safety recomendations.

## The key to encryption
Just like with doors, keys are used to lock (encrypt) and unlock (decrypt) information to keep it safe. But instead of a physical key, an encryption key is an long string of random characters.

As an example, a message with sensitive information needs to be sent securely from one person to another. The sender will encrypt the message with one key, and the receiver will decrypt it with another.


## 1. Symmetric encryption

A symmetric key uses the same string for both encryption and decryption which means that both the sender and receiver need the same key. 

![Symm key Basic](/Images/symm_key_basic.png)

There are [serveral algorithms](History.md) used for symmetric key encryption. In summary, here are the lessons learnt.
1. Caesar's Cipher: Encryption strength should not be derived from secrecy of algorithm.
2. Substitution Cipher: Patterns weaken encryption. 
3. Vigeneres Cipher: Key should not be repeated.
4. Stream Ciphers: Authenticity, key Re-use & low-entropy issues. 
5. Block Ciphers: Current day ciphers. AES or chacha is generally used. (1975 DES, 1976 D-H key Exchange, 1991 IDES, 2002 AES, 2008 ChaCha20)  

![Algos](/Images/algos.png)

#### Challenges with Symmetric Encryption
1. Key Distribution Problem. 
    + This was solved by [Diffie-Hellman](/Encryption%20algorithms/D-H.md) in 1976. This is considered a landmark and the most important discovery in cryptography.
    + Current day, it is adviced to use [Elliptic-Curve](/Encryption%20algorithms/elliptic-curve.md) instead of D-H method. 
2. Does not solve Authenticity.


## 2. Asymmetric encryption

In contrast to symmetric ciphers, there are asymmetric ciphers (also called public-key cryptography). These ciphers use two keys: a public key and a private key. The keys are mathematically related but still distinct. Anything encrypted with the public key can only be decrypted with the private key and data encrypted with the private key can be decrypted with the public key. The public key is widely distributed while the private key is kept secret. If you want to communicate with a given person, you use their public key to encrypt your message and only their private key can decrypt it. 

Two primary usecases for Asymmetric keys
1. **Securely send data** to someone. Anyone can encrypt data with a public key and only owner of private key can open it. 

![Usecase1](/Images/assymetric_usecase1.png)

2. **Authentication** Owner singns data with private key and if it can be decrypted with a public key then it must have originated from the owner.

![Usecase2](/Images/assymetric_usecase2.png)

[RSA](/Encryption%20algorithms/RSA.md) is the current heavyweight champion of asymmetric ciphers and was developed in 1977.

A major downside to asymmetric ciphers is that they are computationally expensive. Can we get authentication with symmetric ciphers to speed things up? If you only share a key with one other person, yes. But that breaks down quickly. Suppose a group of people want to communicate with one another using a symmetric cipher. The group members could establish keys for each unique pairing of members and encrypt messages based on the recipient, but a group of 20 people works out to 190 pairs of members total and 19 keys for each individual to manage and secure. By using an asymmetric cipher, each person only needs to guard their own private key and have access to a listing of public keys.

#### Challenges with Asymmetric Encryption

Asymmetric ciphers are also limited in the amount of data they can encrypt. Like block ciphers, you have to split a longer message into pieces. In practice then, asymmetric ciphers are often used to establish a confidential, authenticated channel which is then used to exchange a shared key for a symmetric cipher. The symmetric cipher is used for subsequent communications since it is much faster. TLS can operate in exactly this fashion. Asymetric encryption is very slow compared to symetric encryption.


## 3. Cryptographic Hash function

A cryptographic hash function is meant to take an input of arbitrary size and type and produce a fixed size binary output (often called a digest). If we can find any two messages that create the same digest, that's a collision and makes the hash function unsuitable for cryptography. If we have an infinite world of messages and a fixed sized output, there are bound to be collisions, but if we can find any two messages that collide **without** a monumental investment of computational resources, that's a deal-breaker. Worse still would be if we could take a specific message and could then find another message that results in a collision. A good hash function has following features:

1. It is a one-way deterministic function aka trapdoor functions. (Same input gives same hash)
2. The output is dependent on all input bits. (Change one bit and everything chagnes)
3. Output is uniformly distributed. 
4. Impossible (difficult) to make a collision.

![hash](/Images/hash_where.png)
![hash algos](/Images/hash_algorithms.png)

As well, the hash function should be **one-way**: given a digest, it should be computationally infeasible to determine what the message is. Respectively, these requirements are called:
1. Pre-image resistance: Given a hash, it should be difficult to find the message from which it was created, even if you know the hash function used.
2. Second pre-image resistance: Given a message, it should be difficult to find another message that, when hashed, generates the same hash.
3. Collision resistance: It should be difficult to find any two messages that generate the same hash.
  
If we meet these requirements, our digest acts as 
1. Digital Signature: A kind of fingerprint for a message. No two people have the same fingerprints, and you can't take a fingerprint and turn it back into a person. [Digital signature using hash function](/Implimentation_code/digital_signature.py)
2. Shadow files (Passwords) : [How do you think passwords are stored in a server?](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/)
3. [HMAC](/Encryption%20algorithms/HMAC.md): Just like digital sign uses Asymmetric keys, HMACS use symetric keys.
4. Make deterministic Unique IDs: Commit id's on git to airflow dag ids - every software application has these.

If we send a message and a digest, the recipient can use the same hash function to generate an independent digest. If the two digests match, they know the message hasn't been altered. SHA-256 is the most popular cryptographic hash function.

- [Implementation of hash using python hashlib](/Implimentation_code/hash.py)
- [MD5 implementation](/Implimentation_code/md5.md)
- [SHA implementation](/Implimentation_code/SHA.md)

# PUTTING IT ALL TOGETHER

| Security goal      | Hash   | HMAC    | Digital Signature | Description |
| :---               | :----: |   :---: |  :---:            | :---
| Integrity          | Y  | Y  | Y             | Can the recipient be confident that the message has not been modified? |
| Authenticity       |    N    | Y   | Y            | Can the recipient be confident that the message originates from the sender? |
| Non-repudation     |     N   |    N     | Y             | Can the sender shouldnt be able to repudite their message? |
| Kind of keys       | NONE   | Symmetric | Asymmetric  |  |

### [Difference between **https** and **http**](/Encryption%20algorithms/https_and_http.md)

For asymmetric ciphers, we have digital signatures. In RSA, encryption with a public key makes something only the private key can decrypt, but the inverse is true as well and can create a type of signature. If only I have the private key and encrypt a document, then only my public key will decrypt the document, and others can implicitly trust that I wrote it: authentication. In fact, we don't even need to encrypt the entire document. If we create a digest of the document, we can then encrypt just the fingerprint. Signing the digest instead of the whole document is faster and solves some problems around the size of a message that can be encrypted using asymmetric encryption. Recipients decrypt the digest, independently calculate the digest for the message, and then compare the two to ensure integrity. 

Now that we have all the major pieces, we can implement a system that has all three of the attributes we're looking for. Alice picks a secret symmetric key and encrypts it with Bob's public key. Then she hashes the resulting ciphertext and uses her private key to sign the digest. Bob receives the ciphertext and the signature, computes the ciphertext's digest and compares it to the digest in the signature he verified using Alice's public key. If the two digests are identical, he knows the symmetric key has integrity and is authenticated. He decrypts the ciphertext with his private key and uses the symmetric key Alice sent him to communicate with her confidentially using HMACs with each message to ensure integrity. There's no protection here against a message being replayed. To handle that issue, we would need some sort of "handshake" that could be used to establish a random, short-lived session identifier.

# THE MISSING PIECE OF PUZZLE

Authentication in the online world relies on public key cryptography where a key has two parts: a private key kept secret by the owner and a public key shared with the world. After the public key encrypts data, only the private key can decrypt it. 

In practice, what is signed is not the actual message, but a digest of a message attained by sending the message through a cryptographic hash function. Instead of signing an entire zip file of source code, the sender signs the 256-bit SHA-256 digest of that zip file and sends the zip file in the clear. Recipients independently calculate the SHA-256 digest of the file they received. They input their digest, the signature they received, and the sender's public key into a signature verification algorithm. If the verification succeeds, the file has not been modified in transit and must have originated from the sender since only the sender has the private key that created the signature. 

There's one major detail missing from this scenario. Where do we get the sender's public key? 

The sender could send the public key along with a message, but then we have no proof of their identity beyond their own assertion. Imagine being a bank teller and a customer walks up and says, "Hello, I'm Jane Doe, and I'd like to make a withdrawal." When you ask for identification, she points to a name tag sticker on her shirt that says "Jane Doe." Personally, I would politely turn "Jane" away.

If you already know the sender, you could meet in person and exchange public keys. If you don't, you could meet in person, examine their passport, and once you are satisfied it is authentic, accept their public key. To make the process more efficient, you could throw a party, invite a bunch of people, examine all their passports, and accept all their public keys. Building off that, if you know Jane Doe and trust her (despite her unusual banking practices), Jane could go to the party, get the public keys, and give them to you. In fact, Jane could just sign the other public keys using her own private key, and then you could use an online repository of public keys, trusting the ones signed by Jane. If a person's public key is signed by multiple people you trust, then you might decide to trust that person as well (even though you don't know them). In this fashion, you can build a web of trust.

But now things have gotten complicated: We need to decide on a standard way to encode a key and the identity associated with that key into a digital bundle we can sign. More properly, these digital bundles are called certificates. We'll also need tooling that can create, use, and manage these certificates. The way we solve these and other requirements is what constitutes a public key infrastructure (PKI).

What if the world had some exceptionally trustworthy people constantly verifying and signing keys for websites? You could just trust them, and browsing the internet would be much smoother. At a high level, that's how things work today. These "exceptionally trustworthy people" are companies called certificate authorities (CAs). When a website wants to get its public key signed, it submits a certificate signing request (CSR) to the CA.

CSRs are like stub certificates that contain a public key and an identity (in this case, the hostname of the server), but are not signed by a CA. Before signing, the CA performs some verification steps. In some cases, the CA merely verifies that the requester controls the domain for the hostname listed in the CSR (via a challenge-and-response email exchange with the address in the WHOIS entry, for example). In other cases, the CA inspects legal documents, like business licenses. Once the CA is satisfied (and usually after the requester has paid a fee), it takes the data from the CSR and signs it with its own private key to create a certificate. The CA then sends the certificate to the requester. The requester installs the certificate on their site's web server, and the certificate is delivered to users when they connect over HTTPS (or any other protocol secured with TLS).

When users connect to the site, their browser looks at the certificate, checks that the hostname in the certificate is the same as the hostname it is connected to (more on this in a moment), and verifies the CA's signature. If any of these steps fail, the browser will show a warning and break off the connection. Otherwise, the browser uses the public key in the certificate to verify some signed information sent from the server to ensure that the server possesses the certificate's private key. These messages also serve as steps in one of several algorithms used to establish a shared secret key that will encrypt subsequent messages. 


![CA](/Images/CA.png)



> *The cryptographic world is vast and complex, but I hope this article gives you a basic mental model of the core goals and components it uses. With a solid foundation in the concepts, you'll be able to continue learning more.*

> --BHARATH K. REDDY