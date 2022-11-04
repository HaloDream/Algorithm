'''
假设中缀表达式是一个由空格分隔的标记字符串。 操作符标记是*，/，+和 - ，以及左右括号。操作数是单字符 A，B，C 等。 以下步骤将后缀顺序生成一个字符串。

    创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。
    通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。
    从左到右扫描标记列表。
        如果标记是操作数，将其附加到输出列表的末尾。
        如果标记是左括号，将其压到 opstack 上。
        如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
        如果标记是运算符，*，/，+或 - ，将其压入 opstack。但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。
    当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。
'''

from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:  # 处理优先级
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


print(infixToPostfix("A*B+C*D"))
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))
print(infixToPostfix("(A+B)*(C+D)"))
