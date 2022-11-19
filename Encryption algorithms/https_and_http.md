# Difference between https and http

Open any http site ex: www.example.com, use ```nslookup www.example.com``` 
to find the ip address of the website, this should match the address on the developer tools network tab.

Wireshark packet capture shows all the communication over **HTTP** to be in :warning: **plain text** :warning:

![http.png](/Images/http.png)


Now open any https site ex: www.instagram.com and do the same what do you see ?

![https.png](/Images/https.png)
![instagram.png](/Images/instagram_https.png)

1. HTTPS is HTTP over TLS
2. TLS sits between TCP and Application layer.
3. All data is sent encrypted over TLS.\
4. Server and Client handshake during TLS establishes the protocol, ciphersuite, and the key using [Diffe-Hellman exchange.](/Encryption%20algorithms/Diffe-hellman.md)

![tls1](/Images/tls1.jpeg)
![tls2](/Images/tls2.jpeg)
![tls3](/Images/tls3.png)
![tls4](/Images/tls4.png)





