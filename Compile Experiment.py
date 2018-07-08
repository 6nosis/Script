#! /usr/bin/env python
# -*- coding:UTF-8 -*-
import prettytable
'''
文法：
 E -> T E´ ①
 E´-> + T {GEQ(+)} E´②| - T {GEQ(-)} E´③| ε ④
 T -> F T´⑤
 T´-> * F {GEQ(*)} T´⑥| / F {GEQ(/)} T´⑦| ε ⑧
 F -> i {PUSH(i)} ⑨ | ( E ) ⑩
其中：
E'--S {GEQ(+)}--O {GEQ(-)}--P ε--N T'--U {GEQ(*)}--Q {GEQ(/)}--V PUSH(i)--R

将产生式右侧按照上面对应关系按编号写入grammar

'''
grammar = ((),"TS","+TOS","-TPS","N","FU","*FQU","/FVU","N","iR","(E)")

#LL(1)分析表
LL1table = {
    ('E','i'):1,
    ('E','('):1,
    ('S','+'):2,
    ('S','-'):3,
    ('S',')'):4,
    ('S','#'):4,
    ('T','i'):5,
    ('T','('):5,
    ('U','+'):8,
    ('U','-'):8,
    ('U','*'):6,
    ('U','/'):7,
    ('U',')'):8,
    ('U','#'):8,
    ('F','i'):9,
    ('F','('):10
}

tb = prettytable.PrettyTable()
tb.field_names = ["SYN[n]", "X", "W", "SEM[m]", "QT[q]"]

#栈的列表实现---
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

    #以列表形式入栈
    def pushlist(self,item):
        self.items.append(item)

    # 把栈顶元素弹出
    def pop(self):
        return self.items.pop()

#如果symbol是终结符号且不是运算符，转为i
def isSymbol(symbol):
    if symbol in ["+","-","*","/","(",")","#"]:
        return symbol
    else:return "i"

def generateQT(order,symbol,left,right):
    Symbol = ""
    if symbol == "Q":
        Symbol = "*"
    elif symbol == "O":
        Symbol = "+"
    elif symbol == "P":
        Symbol = "-"
    elif symbol == "V":
        Symbol = "/"
    return "("+str(order)+")("+Symbol+","+str(left)+","+str(right)+",t"+str(order)+")"

def buftoShow(item):
    buf = item.copy()
    return buf

def LL1Control(toAnalyze,toShow):
    cur = 0#当前分析字符
    q = 1#四元式标号
    SYN = Stack()#语法栈
    SEM = Stack()#语义栈
    QT = Stack()
    SYN.push("#")
    SYN.push("E")
    while True:
        x = SYN.pop()
        w = toAnalyze[cur]
        '''x是非终结符号'''
        if x == "i":
            cur +=1
            SEM.push(w)
        elif x == "#":
            break
        elif x == w:
            cur +=1
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
        elif x == "R":
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
            continue
        elif x in ["O","P","Q","R"]:
            right = SEM.pop()
            left = SEM.pop()
            QT.pushlist(generateQT(q,x,left,right))
            SEM.pushlist("t"+str(q))
            q += 1
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
        #x是非终结符号
        else:
            y = queryTable((x, isSymbol(w)))
            if y != "N":
                SYN.push(y[::-1])
                toShow.add_row([buftoShow(SYN.items), x, w, buftoShow(SEM.items), buftoShow(QT.items)])
            else:
                toShow.add_row([buftoShow(SYN.items), x, w, buftoShow(SEM.items), buftoShow(QT.items)])
                continue

def queryTable(tuple):
    if tuple in LL1table.keys():
        return grammar[LL1table[tuple]]
    else:
        print("error")
        exit(-1)

def main():
    toAnalyze = input("请输入要分析的字符串：\n")
    LL1Control(toAnalyze,tb)
    print(tb)

if __name__ == "__main__":
    main()