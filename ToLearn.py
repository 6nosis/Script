
#Python3字符串转16进制
a = "12345678".encode().hex()
print(a)
print(len(a))
print(bin(16549))
print(str(bin(16549)))

def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '').zfill(16) for c in s])


print(encode("你好"))

print()