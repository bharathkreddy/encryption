# Diffe Hellman key exchange.

## Cryptographic explanation
The simplest and the original implementation of the protocol uses the multiplicative group of integers modulo *p*, where *p* is prime, and *g* is a *primitive root modulo p*. These two values are chosen in this way to ensure that the resulting shared secret can take on any value from 1 to p–1. Here is an example of the protocol, with non-secret values in blue, and secret values in red.

![Dh](/Images/dh.png)

## Secrecy Chart

![secrecy chart](/Images/dh%20secrecy%20chart.png)
