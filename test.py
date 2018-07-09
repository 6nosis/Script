def getOrder(key):
    result = []
    tmp = []
    for i in key:
        tmp.append(ord(i))
    order = tmp.copy()
    order.sort()
    tmporder = set(order)
    for i in tmporder:
        if order.count(i) == 1:
            result.append(tmp.index(i))
        else:
            uniqueindex = unique_index(tmp,i)
            for j in uniqueindex:
                result.append(j)
    return result

def unique_index(L,e):
    return [i for (i,j) in enumerate(L) if j == e]

print(getOrder("experiment"))