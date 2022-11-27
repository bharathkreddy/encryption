# HISTORY OF ENCRYPTION

## 1. CAESAR'S CIPHER

Earlist form of encryption was when cesar sent encrypted messages. Cesars Cipher is just a shift in letters - often called [Caesar cipher](/Implimentation_code/Caesar_cipher.py). The key space here is 26, [here](/Implimentation_code/break_caesar_cipher.py) is how we can break this cipher. Hence the most important rule in cryptography :

>Eve shold not be able to break the ciphers even when she knows the algorithm used.

## 2. SUBSTITUTION CIPHER

To overcome they small key space, ceaser's cipher was soon replaced by [substitution cipher](/Implimentation_code/substitution_cipher.py). Now each alphabet can be substituted by any other alphabet. Although the number of possible substitution alphabets is very large **(26! ≈ 288.4, or about 88 bits)**, this cipher is not very strong, and is easily broken. Provided the message is of reasonable length, the cryptanalyst can deduce the probable meaning of the most common symbols by [analyzing the frequency distribution of the ciphertext](/Implimentation_code/frequency_analysis.py) and using some simple [guesses](/Implimentation_code/frequency_analysis_2.py). This allows formation of partial words, which can be tentatively filled in, progressively expanding the (partial) solution. 


## 3. STREAM CIPHERS

Now the second learning, regardles the key space, the algorithm needs to be strong. We broke the 88 bit substitution cipher but it had a weakness, it had repeatability which caused patterns and these patterns were exploited via frequency analysis. One time pad is technically unbreakable but it is not feasible to be implemented. The closest we come is a stream cipher. We need to understand the [XOR function](/Implimentation_code/XOR.py) and its properties to understand this cipher. 

message XOR random(key_stream) = cipher
cipher XOR random(Key_stream) = message

We see that [stream ciphers](/Implimentation_code/Stream_cipher.py) has below challenges
1. Authenticity - Stream ciphers can be tampered inflightm hence they need something called MAC/Message Authenticity Code to prove the authenticity of sender. 
2. Key re-use issues 
3. Low Entrypy : Low entropy is vulnerable to [brute force attacks.](/Implimentation_code/Stream_cipher.py)

some stream ciphers used - (All algorithms are kept secret. Many claims on these beeing broken, but nothing proved. These are not used anymore)
- A5/1 (G2 ENCRYPTION): 54 BIT [LSFR](https://www.cs.princeton.edu/courses/archive/spring19/cos126/assignments/lfsr/)
- A5/2 (EXPORT VERSION): 17 BIT
- RC4 (WEP, SSL) : 2048 BITS

ONETIME PAD is still the holy grail and is theoretically unbreakable, but it is impossible to implement practically. Above algorithms attempt to weaken some requirements for onetime pad and have various implementations. 


## 4. BLOCK CIPHERS

While stream ciphers encrypt bit by bit, a block cipher takes a block of bits and encrypts the entire block. A mode of operation describes how to repeatedly apply a cipher's single-block operation to securely transform amounts of data larger than a block. Most modes require a unique binary sequence, often called an initialization vector (IV), for each encryption operation. The IV has to be non-repeating and, for some modes, random as well. The initialization vector is used to ensure distinct ciphertexts are produced even when the same plaintext is encrypted multiple times independently with the same key. Block ciphers may be capable of operating on more than one block size, but during transformation the block size is always fixed. Block cipher modes operate on whole blocks and require that the last part of the data be padded to a full block if it is smaller than the current block size. There are, however, modes that do not require padding because they effectively use a block cipher as a stream cipher.

### MODES IN BLOCK CIPHERS

    1. Electronic codebook (ECB)

    The simplest (and not to be used anymore) of the encryption modes is the electronic codebook (ECB) mode . The message is divided into blocks, and each block is encrypted separately. Advantages are both encryption and decryption are parallizable and it allows Random Read Access. 

    The disadvantage of this method is a lack of diffusion. Because ECB encrypts identical plaintext blocks into identical ciphertext blocks, it does not hide data patterns well. ECB is not recommended for use in cryptographic protocols.

    [!ECB](/Images/ECB.png)

    2. Cipher block chaining (CBC)[edit]

    In CBC mode, each block of plaintext is XORed with the previous ciphertext block before being encrypted. This way, each ciphertext block depends on all plaintext blocks processed up to that point. To make each message unique, an initialization vector must be used in the first block.

    [!CBC](/Images/CBC.png)

    Its main drawbacks are that encryption is sequential (i.e., it cannot be parallelized), and that the message must be padded to a multiple of the cipher block size.
    Note that a one-bit change in a plaintext or initialization vector (IV) affects all following ciphertext blocks.

    Decrypting with the incorrect IV causes the first block of plaintext to be corrupt but subsequent plaintext blocks will be correct As a consequence, decryption can be parallelized. 

    [!CBC Example](/Images/CBC_example.png)

    3. Propagating cipher block chaining (PCBC)

    The propagating cipher block chaining or plaintext cipher-block chaining mode was designed to cause small changes in the ciphertext to propagate indefinitely when decrypting, as well as when encrypting. In PCBC mode, each block of plaintext is XORed with both the previous plaintext block and the previous ciphertext block before being encrypted. Like with CBC mode, an initialization vector is used in the first block. Unlike CBC, decrypting PCBC with the incorrect IV (initialization vector) causes all blocks of plaintext to be corrupt.

    [!PCBC](/Images/PCBC.png)

    Cipher feedback (CFB)
    Full-block CFB

    The cipher feedback (CFB) mode, in its simplest form uses the entire output of the block cipher. In this variation, it is very similar to CBC, makes a block cipher into a self-synchronizing stream cipher. CFB decryption in this variation is almost identical to CBC encryption performed in reverse:


##  BLOCK CIPHER ALGORITHMS 
-  [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) 

    56-bit block cipher. You can find the [code here](/Implimentation_code/pyDes.py) and an [usage here](/Implimentation_code/DESexample.py) for both ECB & CBC modes.

-  [AES : Advanced Encryption Standard](/Encryption%20algorithms/AES.md) Current De facto standard. Key lengths 126, 192 and 256. 

    Here is how to generate kyes using [AES (GnuPG)](/Implimentation_code/Symmetric_key_GnuPG.md)

-  [chacha20](https://en.wikipedia.org/wiki/Salsa20): Closest to AES, light weight. 
-  [IDEA : International Data Encryption Algorithm](https://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm) IDEA was originally meant to be a replacement for the DES standard. IDEA uses a 128-bit encryption key
-  [RC5 : Rivest Cipher](https://en.wikipedia.org/wiki/RC4), uses variable length encryption keys ranging up to 2040 bits












