AES is a 128 bit symmetric key block cipher. This means it takes 128 bits of plaintext and converts it into a 128 bit ciphertext. This conversion happens using a key which can be 128 (10 rounds), 192 (12 rounds) or 256(14 rounds) bits. This is based on rijndael algorithm. This is extremely fast. 

The basis for AES or any modern encryption, is SP network which is an s-box ( substitution box ) over a p-box (permutation box).

S-box has arbitary substitution rules as shown to the right, and p-box has arbitary permutations. The size of in and out is called the block size. AES uses 128 bit block. 

![SP NET](https://github.com/bharathkreddy/encryption/blob/main/Images/SP%20Net.png)

Generally SP Nets are reversible, here comes the key. We chain each round of SP net with a key XOR operation.

First the key is exanded and broken down to chunks.

input XOR key chunk1 -> input to SP net in blocks of 128 bits -> XOR key chunk 2 -> repeat round 2 >> continue until rounds enforced by the AES key.

AES is a form of SP net but here are the borad steps takeing
1. bytes are first ordered like this 
![AES bytes](https://github.com/bharathkreddy/encryption/blob/main/Images/AES%20ordering.png)
2. substitue bytes (same as in S of an SP network)
3. Shift rows in below fashion
    - Row 0 stays as is,
    - Row 1 shifts left by 1 (the first bit goes to end)
    - Row 2 shifts left by 2 ... and so on for all rows
4. Mix columns - this is essentially a matrix multiplication of n x n to n x 1 matrix where each element becomes combination of all elements. 
5. Add round 2 keys 
6. Repeat until rounds enforced by the AES key size.
  
