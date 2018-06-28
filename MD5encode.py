import hashlib

# 待加密信息
str = '18602496723'

# 创建md5对象
hl = hashlib.md5()

# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())

'''
or:
from hashlib import md5

UC_KEY = '123456789'
key = md5(UC_KEY.encode('utf-8')).hexdigest()

print(key)
'''