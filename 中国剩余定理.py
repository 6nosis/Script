import gmpy2 as gm

Mod_num = [241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383]
res_list = [119, 203, 213, 175, 5, 91, 146, 251, 277, 175, 127, 299, 102, 260, 275, 224, 329, 27, 242, 23, 343, 85, 184, 21]

# 求M
M = 1
for i in Mod_num:
    M *= i
# print M
# 求Mi
Mi_list = []
for i in Mod_num:
    Mi_list.append(M/i)
# print Mi_list

# 求Mi对mi的逆元
mi_inv_list = []
for i, j in zip(Mi_list, Mod_num):
    mi_inv_list.append(int(gm.invert(i, j)))
# print mi_inv_list

res = 0
for i, j, k in zip(res_list, mi_inv_list, Mi_list):
    res += i*j*k

res = res % M
# print res
print hex(res)[2:-1].decode("hex")
