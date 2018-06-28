


def str2bin(str):
    result = ""
    for i in str:
        result += bin(ord(i)).replace('0b', '').zfill(8)
    return result


print(len(str2bin('¯¢#G²Ob')))
