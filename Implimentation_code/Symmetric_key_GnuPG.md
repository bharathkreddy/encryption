# SYMMETRIC KEYS IMPLIMENTATION USING GnuPG

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
