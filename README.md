# Encryption 

This writeup gives an overview of encryption and describes the differences between two types: symmetric and asymmetric.

## The key to encryption
Just like with doors, keys are used to lock (encrypt) and unlock (decrypt) information to keep it safe. But instead of a physical key, an encryption key is an long string of random characters.

As an example, a message with sensitive information needs to be sent securely from one person to another. The sender will encrypt the message with one key, and the receiver will decrypt it with another.

## 1. Symmetric encryption

A symmetric key uses the same string for both encryption and decryption which means that both the sender and receiver need the same key. This type of encryption is not very safe because sharing the one key in a secure and secretive manner is very difficult to do.

Having said that, using symmetric encryption works well for some tasks, such as moving a file between two computers. And it's a much easier method to begin with than asymmetric encryption.

Some algorithms used are
+ [AES : Advanced Encryption Standard](https://github.com/bharathkreddy/encryption/blob/main/Encryption%20algorithms/AES.md)
+ DES (Advanced Encryption Standard)
+ IDEA (International Data Encryption Algorithm. IDEA was originally meant to be a replacement for the DES standard. IDEA uses a 128-bit encryption key.)
+ RC5 (Rivest Cipher, uses variable length encryption keys ranging up to 2040 bits)

### 1.1 USING GnuPG

1. Install GnuPG
    ```
    sudo apt-get install gnupg2
    brew install gpg
    ```
2. Encrypt the file
    1. -a --armor: ASCII armour: output by gpg is in bytes, this flag converts this output to ASCII for easy sharing and usage. 
    2. -c --symmetric: to enforce a symmetric cipher.
    3. --batch : needed if passphrase is from a file.
    4. --output : to output to a file, if left then the output is streamed to stdout.
    ```
    gpg --symmetric --armor --cipher-algo AES256 --batch --passphrase-file password.txt --output symmetric_encrypted.txt.gpg plaintext.txt
    ```
3. Decrypt the file
    ```
    gpg --decrypt --armor --passphrase-file password.txt --output decrypted.txt symmetric_encrypted.txt.gpg
    ```

### 1.2 USING GnuPG

## 2. Asymmetric encryption

n contrast to symmetric ciphers, there are asymmetric ciphers (also called public-key cryptography). These ciphers use two keys: a public key and a private key. The keys are mathematically related but still distinct. Anything encrypted with the public key can only be decrypted with the private key and data encrypted with the private key can be decrypted with the public key. The public key is widely distributed while the private key is kept secret. If you want to communicate with a given person, you use their public key to encrypt your message and only their private key can decrypt it. RSA is the current heavyweight champion of asymmetric ciphers.

A major downside to asymmetric ciphers is that they are computationally expensive. Can we get authentication with symmetric ciphers to speed things up? If you only share a key with one other person, yes. But that breaks down quickly. Suppose a group of people want to communicate with one another using a symmetric cipher. The group members could establish keys for each unique pairing of members and encrypt messages based on the recipient, but a group of 20 people works out to 190 pairs of members total and 19 keys for each individual to manage and secure. By using an asymmetric cipher, each person only needs to guard their own private key and have access to a listing of public keys.

Asymmetric ciphers are also limited in the amount of data they can encrypt. Like block ciphers, you have to split a longer message into pieces. In practice then, asymmetric ciphers are often used to establish a confidential, authenticated channel which is then used to exchange a shared key for a symmetric cipher. The symmetric cipher is used for subsequent communications since it is much faster. TLS can operate in exactly this fashion.

### 2.1 USING GnuPG
1. Generate Asymmetric keys
    ```
    gpg --generate-key 
    ```
2. Share the public key
    ```
    gpg --armor --export reddybharath.k@gmail.com > brk_public.asc
    ```
3. Import someone else's key
    ```
    gpg --import XYZ.asc
    ```
4. view list of own keys
    ```
    gpg --list-secret-keys 
    ```
5. Verify keys with fingerprints
    You will want to make sure that the public keys you have belong to the people you think they do. Checking the validity of your public keys can be tricky. The easiest way is to import the key in question and then verify it by talking to its owner face-to-face or by phone.

    Of course, reading aloud the many lines of random characters that a key is composed of would take a lot of time and leave room for making errors. Instead, you can verify the fingerprint which is a much shorter representation of a public key.

    This command returns a list of fingerprints for all public keys that you have imported:
    ```
    gpg --fingerprint
    ```

6. Encrypt a message
    Create a text file with your preferred text editor and save it. Back in the terminal, navigate to where you saved the file. Run the following command. Replace the email to that of recipient. This generates plaintext.txt.asc
    ```
    gpg --armor --encrypt --recipient xyz@email.com plaintext.txt
    ```
7. Decrypt a message from a friend
    Since your private key will be used to decrypt the message and because your private key is password protected, you will be prompted to enter the password ( in our case bharath ). This will generate decrypted text in file called gpg_decrypted.txt
    ```
    gpg --decrypt plaintext.txt.asc > gpg_decrypted.txt
    ```

### 2.2 USING openssl

1. check current verison of openssl
    ```
    openssl version
    ```
2. Generate key pair 
    - openssl genrsa : generate rsa key
    - aes256: Encrypt PEM output with CBC AES. If security is important, note that a private key should almost always be encrypted AND kept in a secure place. If we open brk_private.pem we would see the first two lines telling its ecrypted and giving the cypher used to encrypt the file. After entering the command, OpenSSL prompts user for a passphrase, which they must enter each time they wants to use the keys.
    - out file: Output the key to 'file'
    - 1024: keysize in bits
    - if we want openssl to take password for aes encryption from a file we can add -passout flag. 
    ```
    openssl genrsa -aes256 -passout file:password.txt -out brk_private.pem 1024
    ```
3. we can see the brk_private.pem produced but this is ecrypted. To see the decrypted version of the file 
    - Enter below command and openssl would ask for the password in same termainal
    ```
    openssl rsa -in brk_private.pem -noout -text 
    ```
    - Use below command to pass in the file with password.
    ```
    openssl rsa -in brk_private.pem -passin file:password.txt -noout -text 
    ```
4. Extract the public key details in same way as above but in a file which can then be shared as a public key. 
    - pass in the password file and write out the public key
    ``` 
    openssl rsa -in brk_private.pem -passin file:password.txt -pubout > brk_public.pem
    ```
5. the files are rendedred in hexdecimal but can be viewed in same way but this time pass in the public key
    ```
    openssl rsa -in brk_public.pem -pubin -noout -text
    ```
6. ENCRYPT the message but points to note
    - RSA can encrypt a file no larger than the size of the modulus i.e. key length. 
    - usually only keys are ecrypted using RSA and once authentication is established a symertic key is used to encrypt the files using diffie-hellman method.
    - Our file is small and hence we can ecrypt it using.
    ```
    openssl rsautl -sign -inkey brk_private.pem -passin file:password.txt -in file.txt -out encrypted_file.txt
    ```
    - this creates the encrypted file in binary encoding but we can also do this in base64 encoding if needed. 

7. Decrypt the file. 
    - cat the contents of encrypted file to be sure its encrypted. 
    - hedump displays the contents of binary files in hexadecimal, decimal, octal, or ASCII.
    ``` 
    hexdump -C ./ecrypted_file.txt
    ```
    -  Decrypt the key using public key
    ```
    openssl rsautl -verify -pubin -inkey brk_public.pem -in encrypted_file.txt -out decrypted_file.txt
    ```

8. to ecrypt using public key and decrypt using private key
    ```
    openssl rsautl -encrypt -inkey public_key.pem -pubin -in <decrypted file> -out <encrypted file>
    openssl rsautl -decrypt -inkey private_key.pem -in <encrypted file> -out <decrypted file>
    ```

## 3. Cryptographic Hash function

A cryptographic hash function is meant to take an input of arbitrary size and produce a fixed size output (often called a digest). If we can find any two messages that create the same digest, that's a collision and makes the hash function unsuitable for cryptography. Note the emphasis on "find"; if we have an infinite world of messages and a fixed sized output, there are bound to be collisions, but if we can find any two messages that collide without a monumental investment of computational resources, that's a deal-breaker. Worse still would be if we could take a specific message and could then find another message that results in a collision.

As well, the hash function should be one-way: given a digest, it should be computationally infeasible to determine what the message is. Respectively, these requirements are called collision resistance, and preimage resistance. If we meet these requirements, our digest acts as a kind of fingerprint for a message. No two people (in theory) have the same fingerprints, and you can't take a fingerprint and turn it back into a person.

If we send a message and a digest, the recipient can use the same hash function to generate an independent digest. If the two digests match, they know the message hasn't been altered. SHA-256 is the most popular cryptographic hash function.



## 4. Message Authentication Codes

Hashes sound great, but what good is sending a digest with a message if someone can tamper with your message and then tamper with the digest too? We need to mix hashing in with the ciphers we have. For symmetric ciphers, we have message authentication codes (MACs). MACs come in different forms, but an HMAC is based on hashing. An HMAC takes the key K and the message M and blends them together using a hashing function H with the formula H(K + H(K + M)) where "+" is concatenation. Why this formula specifically? That's beyond this article, but it has to do with protecting the integrity of the HMAC itself. The MAC is sent along with an encrypted message. Eve could blindly manipulate the message, but as soon as Bob independently calculates the MAC and compares it to the MAC he received, he'll realize the message has been tampered with.

## PUTTING IT ALL TOGETHER

For asymmetric ciphers, we have digital signatures. In RSA, encryption with a public key makes something only the private key can decrypt, but the inverse is true as well and can create a type of signature. If only I have the private key and encrypt a document, then only my public key will decrypt the document, and others can implicitly trust that I wrote it: authentication. In fact, we don't even need to encrypt the entire document. If we create a digest of the document, we can then encrypt just the fingerprint. Signing the digest instead of the whole document is faster and solves some problems around the size of a message that can be encrypted using asymmetric encryption. Recipients decrypt the digest, independently calculate the digest for the message, and then compare the two to ensure integrity. The method for digital signatures varies for other asymmetric ciphers, but the concept of using the public key to verify a signature remains.

Now that we have all the major pieces, we can implement a system that has all three of the attributes we're looking for. Alice picks a secret symmetric key and encrypts it with Bob's public key. Then she hashes the resulting ciphertext and uses her private key to sign the digest. Bob receives the ciphertext and the signature, computes the ciphertext's digest and compares it to the digest in the signature he verified using Alice's public key. If the two digests are identical, he knows the symmetric key has integrity and is authenticated. He decrypts the ciphertext with his private key and uses the symmetric key Alice sent him to communicate with her confidentially using HMACs with each message to ensure integrity. There's no protection here against a message being replayed (as seen in the ice cream disaster Eve caused). To handle that issue, we would need some sort of "handshake" that could be used to establish a random, short-lived session identifier.

*The cryptographic world is vast and complex, but I hope this article gives you a basic mental model of the core goals and components it uses. With a solid foundation in the concepts, you'll be able to continue learning more.*

> --BHARATH K. REDDY

---

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
