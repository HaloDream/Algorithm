from pythonds.basic.stack import Stack

#检查同类括号是否匹配
def parChecker1(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()

        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False

print(parChecker1("(())"))
print(parChecker1("((()()())"))


#检查不同种类括号之间是否匹配
def parChecker2(symbolString):
    s=Stack()
    balance = True
    index = 0
    while index<len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance =False
            else:
                top=s.pop()

                if not matches(top,symbol):
                    balance=False
        index=index+1

    if balance and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens="({["
    closers=")}]"
    return opens.index(open)==closers.index(close)

print(parChecker2("{{{[]()}}}"))
print(parChecker2("{{{[(]()}}}"))
