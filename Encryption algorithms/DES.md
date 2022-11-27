# DATA ENCRYPTION STANDARD (Original - 1975, Tripple DES - 2005)

DES is a block cipher — an algorithm that takes a fixed-length string of plaintext bits and transforms it through a series of complicated operations into another ciphertext bitstring of the same length. In the case of DES, the block size is 64 bits. DES also uses a key to customize the transformation, so that decryption can supposedly only be performed by those who know the particular key used to encrypt. The key ostensibly consists of 64 bits; however, only 56 of these are actually used by the algorithm. Eight bits are used solely for checking parity, and are thereafter discarded. Hence the effective key length is 56 bits.

Developed jointly by IBM and NSA. In February 1997, RSA Data Security ran a brute force competition with a $10,000 prize to demonstrate the weakness of 56-bit encryption; the contest was won four months later. By current day compute - it can be bruteforced in under 4 hours. 

Like other block ciphers, DES by itself is not a secure means of encryption, but must instead be used in a mode of operation.

You can find the [code here](/Implimentation_code/pyDes.py) and an [usage here](/Implimentation_code/DESexample.py) for both ECB & CBC modes.

### OVER ALL STRUCTURE

The algorithm's overall takes a block of 64 bit plaintext and 56 bit key and converts to 64 bit cipher text. As shown in [!Figure](/Images/DES_overall.png): there are 16 identical stages of processing, termed rounds. There is also an initial and final permutation, termed IP and FP, which are inverses (IP "undoes" the action of FP, and vice versa). IP and FP have no cryptographic significance, but were included in order to facilitate loading blocks in and out of mid-1970s 8-bit based hardware.

1. Key discarding process. Every 8th bit of a 64 bit key is discarding leaving a 56 bit key. 
2. 64-bit plain text block is given to Initial Permutation (IP) function.
3. IP performed on 64-bit plain text block.
4. IP produced two halves of the permuted block known as Left Plain Text (LPT) and Right Plain Text (RPT).
5. Each LPT and RPT performed 16-rounds of encryption process.
6. LPT and RPT rejoined and Final Permutation (FP) is performed on combined block.
7. 64-bit Cipher text block is generated.

Before the main rounds, the block is divided into two 32-bit halves and processed alternately; this criss-crossing is known as the Feistel scheme. The Feistel structure ensures that decryption and encryption are very similar processes—the only difference is that the subkeys are applied in the reverse order when decrypting. The rest of the algorithm is identical. This greatly simplifies implementation, particularly in hardware, as there is no need for separate encryption and decryption algorithms.

The ⊕ symbol denotes the exclusive-OR (XOR) operation. The F-function scrambles half a block together with some of the key. The output from the F-function is then combined with the other half of the block, and the halves are swapped before the next round. After the final round, the halves are swapped; this is a feature of the Feistel structure which makes encryption and decryption similar processes.

- Some useful material [here](https://www.chiragbhalodia.com/2021/09/des-algorithm.html)



