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

#创建最后要显示的表
tb = prettytable.PrettyTable()
tb.field_names = ["SYN[n]", "X", "W", "SEM[m]", "QT[q]"]#添加表头

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
    #以整体形式入栈
    def pushEntirely(self, item):
        self.items.append(item)
    # 把栈顶元素弹出
    def pop(self):
        return self.items.pop()

#如果symbol是终结符号且不是运算符，转为i
def isSymbol(symbol):
    if symbol in ["+","-","*","/","(",")","#"]:
        return symbol
    else:return "i"

#产生四元式
def generateQT(order,symbol,left,right):
    Symbol = ""
    '''将加减乘除变回原样'''
    if symbol == "Q":
        Symbol = "*"
    elif symbol == "O":
        Symbol = "+"
    elif symbol == "P":
        Symbol = "-"
    elif symbol == "V":
        Symbol = "/"
    return "("+str(order)+")("+Symbol+","+str(left)+","+str(right)+",t"+str(order)+")"

#为列表中的项保存副本
def buftoShow(item):
    buf = item.copy()
    return buf

#LL1分析程序，toShow的add_row方法均是将当前各栈的情况添加进表中
def LL1Control(toAnalyze,toShow):
    cur = 0#当前分析字符
    q = 1#四元式标号
    SYN = Stack()#语法栈
    SEM = Stack()#语义栈
    QT = Stack()#四元式栈
    SYN.push("#")
    SYN.push("E")
    while True:
        x = SYN.pop()#弹出x
        w = toAnalyze[cur]#当前分析的字符
        '''x是非终结符号'''
        if x == "i":#如果x是变量则将当前字符入语义栈
            cur +=1
            SEM.push(w)
        elif x == "#":#分析结束跳出
            break
        elif x == w:#如果x是和w相等，直接进行下一个
            cur +=1
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
        elif x == "R":#如果x是push(i)直接下一轮，因为push(i)和i是一起出现的，出现i时已进行下一个
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
            continue
        elif x in ["O","P","Q","R"]:#如果x是加减乘除
            right = SEM.pop()#第一个元素出语义栈作为右操作数
            left = SEM.pop()#第二个元素出语义栈作为左操作数
            QT.pushEntirely(generateQT(q, x, left, right))#生成四元式入四元式栈
            SEM.pushEntirely("t" + str(q))
            q += 1
            toShow.add_row([buftoShow(SYN.items),x,w,buftoShow(SEM.items),buftoShow(QT.items)])
        #x是非终结符号
        else:
            y = queryTable((x, isSymbol(w)))#查询LL1分析表
            if y != "N":#如果不是ε
                SYN.push(y[::-1])#逆序压入语法栈
                toShow.add_row([buftoShow(SYN.items), x, w, buftoShow(SEM.items), buftoShow(QT.items)])
            else:#是ε则跳过
                toShow.add_row([buftoShow(SYN.items), x, w, buftoShow(SEM.items), buftoShow(QT.items)])
                continue

#查询LL1分析表
def queryTable(tuple):
    if tuple in LL1table.keys():#如果查询的元组在字典键中
        return grammar[LL1table[tuple]]
    else:#如果不在字典键中
        print("error")
        exit(-1)

def main():
    toAnalyze = input("请输入要分析的字符串：\n")
    LL1Control(toAnalyze,tb)
    print(tb)

if __name__ == "__main__":
    main()