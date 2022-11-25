import random

def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])

def XOR_bytes(key_stream, message):
    length= min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


# done by enemy
message = "DO ATTACK"
message = message.encode()  # we need to do this as we are xor'ing with bytes and we need message in bytes as well.
key_stream = generate_key_stream(len(message))
cipher = XOR_bytes(key_stream, message)
print('original message: ',message)
print('key_stream: ', key_stream)
print('cipher: ',cipher)
decoded_message = XOR_bytes(key_stream,cipher)
print('decoded message: ',decoded_message)

#this is us trying to break it
print(cipher)
guess_key_steam = generate_key_stream(len(cipher))
text = XOR_bytes(guess_key_steam,cipher)
print(text)



