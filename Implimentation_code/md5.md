# MD5 ( Message Digest 5)

MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4. MD5 is not suitable for applications like SSL certificates or digital signatures that rely on collision resistance property for digital security. collision resistance is a property of cryptographic hash functions: a hash function H is collision-resistant if it is hard to find two inputs that hash to the same output.



1. Lets hash a file : file.txt
2. use below command
    ```
    md5 file.txt
    ```
3. The output should be 
    ```
    MD5 (file.txt) = 986ae684aad2ffd0bb7257deda7882bf
    ```
4. The output is in hexadecimal so each characer is 4 bits long. so 32 hex chars = 128 bits / 16 Bytes

### THEORY
MD5 processes a variable-length message into a fixed-length output of 128 bits. The input message is broken up into chunks of 512-bit blocks (sixteen 32-bit words); the message is padded so that its length is divisible by 512. The padding works as follows: first, a single bit, 1, is appended to the end of the message. This is followed by as many zeros as are required to bring the length of the message up to 64 bits fewer than a multiple of 512. The remaining bits are filled up with 64 bits representing the length of the original message, modulo 264.

The main MD5 algorithm operates on a 128-bit state, divided into four 32-bit words, denoted A, B, C, and D. These are initialized to certain fixed constants. The main algorithm then uses each 512-bit message block in turn to modify the state. The processing of a message block consists of four similar stages, termed rounds; each round is composed of 16 similar operations based on a non-linear function F, modular addition, and left rotation. Figure 1 illustrates one operation within a round. There are four possible functions; a different one is used in each round

![MD5_1](/Images/md5_algo.png)

![MD5_2](/Images/MD5_algorithm.png)


