# Elliptic-curve cryptography (ECC)

Elliptic-curve cryptography (ECC) is an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. ECC allows smaller keys compared to non-EC cryptography (based on plain Galois fields) to provide equivalent security. The U.S. National Institute of Standards and Technology (NIST) has endorsed elliptic curve cryptography in its Suite B set of recommended algorithms, specifically elliptic-curve Diffie–Hellman (ECDH) for key exchange and Elliptic Curve Digital Signature Algorithm (ECDSA) for digital signature.

The primary benefit promised by elliptic curve cryptography is a smaller key size, reducing storage and transmission requirements i.e. that an elliptic curve group could provide the same level of security afforded by an RSA-based system with a large modulus and correspondingly larger key: for example, a 256-bit elliptic curve public key should provide comparable security to a 3072-bit RSA public key.

An elliptic curve is the set of points that satisfy a specific mathematical equation. The equation for an elliptic curve looks something like this:

$ y^2  = x^3 + ax + b $ where a,b are the parameters of the curve. These curves get names depending on values of a & B ex: 
+ NIST P-256: y^2 = x^3-3x+41058363725152142129326129780047268409114441015993725554835256314039467401291 & modulo p = 2^256 - 2^224 + 2^192 + 2^96 - 1 , 
+ X25519: y^2 = x^3+48662x^2+x & modulo p = 2^2252+ 27742317777372353535851937790883648493 (modulo p is order i.e. after how many numbers we return to start point of curve. )

![EC](/Images/Elliptic_curve.png)

While D-H method uses modular arithmetic to have generator work, Elliptic curves starts with any point on the curve g. If g is added to itself, it is the point opposite to a tagent from g cutting the curve. 3g(g+g+g) can be found by drawing a line between g and 2g and 3g is the point opposite where this line cuts the curve, and so on..

So we are able to move around the curve at random fashion just as how we were moving around the modulus circle at random.

so if we get a point on curve its impossible to calculate "?"g this "?" is our private no. Similar to how a & b were in D-H system. 


