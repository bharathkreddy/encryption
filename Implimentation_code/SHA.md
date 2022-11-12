# Hash function

Converts any information like 'abc' to '101101...' 

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
sha256sum FILE > output.txt or sha512sum FILE > output.txt
md5sum FILE > output.txt
```




