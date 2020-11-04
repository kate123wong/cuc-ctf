import binascii
a = int('01101011011011110110010101101011011010100011001101110011',2)
b = hex(a)
c = b.split("0x")
ans = binascii.a2b_hex(c[1])
print(ans)