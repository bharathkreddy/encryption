# import enchant
# dict_check = enchant.Dict("en_US")

def get_key(n):
    key={}
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    for i in letters:
        key[i] = letters[(count+n) % len(letters)]
        count += 1
    return key



def break_cipher(cipher_text):
    for i in range(26):
        key = get_key(i)
        plain_text=[]
        for j in cipher_text:
            if j in key:
                plain_text.append(key[j])
            else:
                plain_text.append(j)
        plain_text = ''.join(plain_text)
        print('attempt {}: {}'.format(i,plain_text))


cipher_text = 'BRX DUH WHUULEOH'
break_cipher(cipher_text)

