#使用栈实现进制转换
#十进制转二进
from pythonds import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber>0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber =decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())
    return binString

print(divideBy2(42))

#任意基数进制转换
def baseConverter(decNumber,base):
    digits="01234567789ABCDEF"

    remstack = Stack()
    while decNumber>0:
        rem= decNumber%base
        remstack.push(rem)
        decNumber=decNumber//base

    newString = ""
    while not remstack.isEmpty():
        newString=newString+str(digits[remstack.pop()])
    return newString
print(baseConverter(23,16))