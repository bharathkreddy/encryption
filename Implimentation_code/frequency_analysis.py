cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

class Attack():
    def __init__(self) -> None:
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.english_frequency = {'e': 0.121607, 'm': 0.0401, 'a': 0.085, 'h': 0.030034, 
        'r': 0.0759, 'g': 0.0247, 'i': 0.07545, 'b': 0.02072, 'k': 0.008, 'o': 0.071635, 
        'f': 0.0181, 't': 0.0695, 'y': 0.0178, 'l': 0.0403, 'n': 0.066544, 'w': 0.012899, 
        's': 0.054893, 'v': 0.010074, 'c': 0.045388, 'x': 0.0029, 'u': 0.036308, 
        'z': 0.00271, 'd': 0.033844, 'j': 0.001965, 'p': 0.03167, 'q': 0.00196} #source : https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
        self.cipher_freq = {}
        self.freq_map = {}
        self.available_cipher_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.available_english_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.key ={}

    def calc_cipher_freq(self,cipher):
        count_cipher_letters = 0
        for x in self.alphabet:
            self.cipher_freq[x]=0
        for x in cipher:
            if x in self.alphabet:
                if x in self.cipher_freq:
                    self.cipher_freq[x] += 1
                else:
                    self.cipher_freq[x] = 1
            count_cipher_letters += 1
        for x in self.cipher_freq:
            self.cipher_freq[x] = round((self.cipher_freq[x] / count_cipher_letters),4)

    def create_freq_map(self):
        for cipher_letter in self.cipher_freq:
            map = {}
            for eng_letter in self.english_frequency:
                map[eng_letter] = round(abs(self.cipher_freq[cipher_letter] - self.english_frequency[eng_letter]),4)
            self.freq_map[cipher_letter] = sorted(map.items(),key=lambda x:x[1])

    def better_guess(self,cipher_letter,english_letter):
        self.key[cipher_letter] = english_letter
        self.available_cipher_letters.replace(cipher_letter,"")
        self.available_english_letters.replace(english_letter,"")

    
    def guess_key(self):
        for cipher_letter in self.available_cipher_letters:
            for english_letter, diff in self.freq_map[cipher_letter]:
                if english_letter in self.available_english_letters:
                    self.key[cipher_letter]= english_letter
                    self.available_english_letters = self.available_english_letters.replace(english_letter,"")
                    break

def decrypt(cipher,key):
    msg = ""
    for x in cipher:
        if x in key:
            msg += key[x]
        else:
            msg += x
    return msg

attack = Attack()
attack.calc_cipher_freq(cipher=cipher)
attack.create_freq_map()
# l>v ; b>a ; u>h ; x/y>g ; d/h>h ; o>k ; 
attack.better_guess('b','a')
attack.better_guess('l','v')
attack.better_guess('u','h')
attack.guess_key()
print(attack.key)
plain_text = decrypt(cipher=cipher,key=attack.key)
P = plain_text.splitlines()
C= cipher.splitlines()
for x in range(len(plain_text.splitlines())):
    print("P :",P[x])
    print("C :",C[x])
    print()