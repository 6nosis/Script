from Crypto.Cipher import DES
import binascii

a = DES.new("12345678")
b = a.encrypt("abcdefgh")

print(binascii.b2a_hex(b))

