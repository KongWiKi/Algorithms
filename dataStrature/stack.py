"""
@time : 2019/8/5下午4:30
@Author: kongwiki
@File: stack.py
@Email: kongwiki@163.com
"""
"""
栈
特性: 先进后出
适用范围：
1. 浏览器的浏览返回
抽象数据类型：
1. Stack() 创建一个空的新栈 并返回一个栈
2. push(item)  将一个新的元素入栈 不返回任何内容
3. pop() 弹出栈顶元素 返回当前栈顶元素
4. peek() 获得当前栈的顶部元素 返回当前栈顶元素
5. isEmpty 判断是否为空 返回布尔值
6. size() 栈长

以下代码实现了如下功能
1. 符号匹配
2. 十进制转化为二进制
3. 中前后缀表达式
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        判断和[]的比较 相同则当前的栈为空 否则不空
        :return: bool
        """
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def pairCheck(symbolString):
    """
    匹配()
    :param symbolString:
    :return:
    """
    s = Stack()
    balenced = True
    index = 0
    while index < len(symbolString) and balenced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced = False
            else:
                s.pop()
        index += 1
    if balenced and s.isEmpty():
        return True
    else:
        return False


def pairCheckII(symbolString):
    """
    匹配({[]})
    :param symbolString:
    :return:
    """
    s = Stack()
    balenced = True
    index = 0
    while index < len(symbolString) and balenced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced = False
            else:
                top = s.pop()
                if not match(s.peek(), top):
                    balenced = False
    index += 1
    if balenced and s.isEmpty():
        return True
    else:
        return False


def match(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)


def divideBy2(devNumber):
    remstack = Stack()
    while devNumber > 0:
        rem = devNumber % 2
        remstack.push(rem)
        devNumber = devNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


def baseConvert(decNumber, base):
    digits =  "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber%base
        remstack.push(rem)
        decNumber = decNumber//base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    return newString


if __name__ == '__main__':
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # s.push('cat')
    # print("当前栈的元素有{}".format(s.items))
    # print("栈顶元素为{}".format(s.peek()))
    # s.pop()
    # print("弹出栈顶元素之后 栈的元素有{}".format(s.items))
    # print("当前栈长为{}".format(s.size()))
    # print("当期栈是否为空 {}".format(s.isEmpty()))
    # string = '((()))'
    # string1 = '(((()))'
    # print(pairCheck(string1))
    # print(divideBy2(8))
