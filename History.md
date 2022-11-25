# HISTORY OF ENCRYPTION

## CAESAR'S CIPHER

Earlist form of encryption was when cesar sent encrypted messages. Cesars Cipher is just a shift in letters - often called [Caesar cipher](/Implimentation_code/Caesar_cipher.py). The key space here is 26, [here](/Implimentation_code/break_caesar_cipher.py) is how we can break this cipher. Hence the most important rule in cryptography :

>Eve shold not be able to break the ciphers even when she knows the algorithm used.

## SUBSTITUTION CIPHER

To overcome they small key space, ceaser's cipher was soon replaced by [substitution cipher](/Implimentation_code/substitution_cipher.py). Now each alphabet can be substituted by any other alphabet. Although the number of possible substitution alphabets is very large **(26! ≈ 288.4, or about 88 bits)**, this cipher is not very strong, and is easily broken. Provided the message is of reasonable length, the cryptanalyst can deduce the probable meaning of the most common symbols by [analyzing the frequency distribution of the ciphertext](/Implimentation_code/frequency_analysis.py) and using some simple [guesses](/Implimentation_code/frequency_analysis_2.py). This allows formation of partial words, which can be tentatively filled in, progressively expanding the (partial) solution. 


## STREAM CIPHERS

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


## BLOCK CIPHERS

While stream ciphers encrypt bit by bit, a block cipher takes a block of bits and encrypts the entire block. 








