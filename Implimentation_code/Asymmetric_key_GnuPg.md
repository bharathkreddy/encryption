# Asymmetric key implementation using GnuPG

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