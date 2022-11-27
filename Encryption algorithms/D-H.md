# Diffie-Helman Key Exchange System. 

Alice and Bob choose a generator g and a large prime p (generator ^ i mod p : generates a set of integers 1 to p-1 in random order, where i is set of all integers.). Alice creates a secret "a" and Bob also creates his secret "b". Alice generates g^a mod p and sends to Bob, and bob sends g^b mod p. Alice and bob each now have a shared secret : g^ab mod p.

![DH1](/Images/Diffie-helman.png)
![DH2](/Images/dh.png)
![DH3](/Images/Diffie-Hellman_Key_Exchange.png)
![DH4](/Images/dh%20secrecy%20chart.png)

[Implementation of Diffie Helman Key exchange.](/Implimentation_code/Diffie_helman.py)
