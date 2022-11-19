# SHA (Secure Hash )

The Secure Hash Algorithms are a family of cryptographic hash functions published by the National Institute of Standards and Technology (NIST) as a U.S. Federal Information Processing Standard (FIPS), including:

SHA-0: A retronym applied to the original version of the 160-bit hash function published in 1993 under the name "SHA". It was withdrawn shortly after publication due to an undisclosed "significant flaw" and replaced by the slightly revised version SHA-1.

SHA-1: A 160-bit hash function which resembles the earlier MD5 algorithm. This was designed by the National Security Agency (NSA) to be part of the Digital Signature Algorithm. Cryptographic weaknesses were discovered in SHA-1, and the standard was no longer approved for most cryptographic uses after 2010.

SHA-2: A family of two similar hash functions, with different block sizes, known as SHA-256 and SHA-512. They differ in the word size; SHA-256 uses 32-bit words where SHA-512 uses 64-bit words. There are also truncated versions of each standard, known as SHA-224, SHA-384, SHA-512/224 and SHA-512/256. These were also designed by the NSA.

SHA-3: A hash function formerly called Keccak, chosen in 2012 after a public competition among non-NSA designers. It supports the same hash lengths as SHA-2, and its internal structure differs significantly from the rest of the SHA family.

### Important properties of hashing algorithm
1. Pseudo Random: ABC should not look like 101101.... 
2. Small change in input drastically changes the hash.
3. Given a hash original input cant be computed.

### IMPLIMENATION: WINDOWS
```
certutil -hashfile "filename.exe" MD5
certutil -hashfile "filename.exe" SHA1
certutil -hashfile "filename.exe" SHA256
certutil -hashfile "filename.exe" SHA512
```
### IMPLIMENTATION: LINUX

```
$ shasum file.txt   # default is sha1 
e7edd002a50c7641a5955610b278e7b5f0274106

$ shasum -a 256 file.txt
c960376012b88cf4cc540c9399890752af876e9395127f43ea3a70270a3f2354

$ shasum -a 512 file.txt
48277be8c795892c746b68f4174e6b48bf348eb19025c5161c948b75f8bc29649c3848514ab86173d3336cc4927a6306e45a00ca98412949f10bcecabf75b0b3
```







