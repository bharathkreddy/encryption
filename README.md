#Encryption - assymetric key
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
    openssl rsa -in alice_private.pem -pubout
    ```
5. the files are rendedred in hexdecimal but can be viewed in same way but this time pass in the public key
```
openssl rsa -in brk_public.pem -pubin -noout -text
```
6. 