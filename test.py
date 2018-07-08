#栈的列表实现
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面,如果是字符串，则一个一个进栈
    def push(self, item):
        if len(item)==1:
            self.items.append(item)
        else:
            for i in item:
                self.items.append(i)

    # 把栈顶元素弹出
    def pop(self):
        return self.items.pop()


a = Stack()

a.push("hello")

a.push("k")
k = a.pop()
print(a.items)
print(k)

def generateQT(order,symbol,left,right):
    return "("+str(order)+")("+symbol+","+left+","+right+",t"+str(order)+")"

print(generateQT(1,'*',"b","c"))