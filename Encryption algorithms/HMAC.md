# HMACs : Hash-based Message Authentication Code.

Hashes sound great, but what good is sending a digest with a message if someone can tamper with your message and then tamper with the digest too? We need to mix hashing in with the ciphers we have. For symmetric ciphers, we have message authentication codes (MACs). MACs come in different forms, but an HMAC is based on hashing. An HMAC takes the key K and the message M and blends them together using a hashing function H with the formula H(K + H(K + M)) where "+" is concatenation. Why this formula specifically? It has to do with protecting the integrity of the HMAC itself. The MAC is sent along with an encrypted message. Eve could blindly manipulate the message, but as soon as Bob independently calculates the MAC and compares it to the MAC he received, he'll realize the message has been tampered with. This is because EVE does not have the shared key which ALICE and BOB has. 

![HMAC](/Images/HMAC.png)

[Pure python implementation of HMAC](/Implimentation_code/HMAC.py)
