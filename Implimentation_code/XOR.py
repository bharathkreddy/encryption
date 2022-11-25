# XOR Function between a & b flips the bits of a, where b is 1 and leaves a intact where b is 0 

### TRUTH TABLE ####
#  a   b   XOR
#  0   0    0
#  0   1    1
#  1   0    1
#  1   1    0

def XOR(a,b):
    print('DECIMALS: ',a,' XOR ',b,' = ',a ^ b)
    print('BINARY: ',bin(a),' XOR ',bin(b),' = ',bin(a ^ b))

XOR(4, 8)
XOR(4, 4)
XOR(255, 1)
XOR(255, 128)




