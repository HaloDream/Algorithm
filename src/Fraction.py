#求最大公约数
def gcd(m,n):
    while m%n !=  0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

#定义分数类
class Fraction:
    #构造函数，定义num分子、den分母
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    #重写str方法，将对象转换成字符串
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    #定义show()方法，将Fraction对象打印为字符串
    def show(self):
        print(self.num,"/",self.den)

    #重写__add__()方法，定义"+"运算功能
    def __add__(self, otherFracton):
        newnum = self.num * otherFracton.den + self.den * otherFracton.num
        newden = self.den * otherFracton.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    #重写__eq__()方法,判断深相等
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

x = Fraction(1,2)
y = Fraction(3,4)

print(x+y)
print(x==y)