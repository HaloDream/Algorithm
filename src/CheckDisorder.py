'''
乱序字符串是指一个字符串只是另一个字符串的重新排列
例如，“python”和“typhon”
为了简单起见，我们假设所所讨论的两个字符串具有相等的长度，并且他们由 26 个小写字母集合组成。
我们的目标是写一个布尔函数，它将两个字符串做参数并返回它们是不是乱序。
'''
'''
我们对乱序问题的第一个解法是检查第一个字符串是不是出现在第二个字符串中。
如果可以检验到每一个字符，那这两个字符串一定是乱序。
可以通过用 None 替换字符来了解一个字符是否完成检查。
但是，由于 Python 字符串是不可变的，所以第一步是将第二个字符串转换为列表。
检查第一个字符串中的每个字符是否存在于第二个列表中，如果存在，替换成 None.
'''


def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            stillOK = False
    # python2.X中使用下列方法len(filter(...))
    # return stillOK and (len(filter(None, alist)) == 0)

    return stillOK and (len(list(filter(lambda x: x != None, alist))) == 0)

print(anagramSolution1('abcd', 'dcba'))

'''
另一个解决方案是利用这么一个事实：即使 s1,s2 不同，它们都是由完全相同的字符组成的。
所以，我们按照字母顺序从 a 到 z 排列每个字符串，如果两个字符串相同，那这两个字符串就是乱序字符串。
'''
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos<len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos+=1
        else:
            matches = False
    return matches

print(anagramSolution2("abcde","dcabe"))

'''
我们最终的解决方法是利用两个乱序字符串具有相同数目的 a, b, c 等字符的事实。
我们首先计算的是每个字母出现的次数。由于有 26 个可能的字符，我们就用 一个长度为 26 的列表，每个可能的字符占一个位置。
每次看到一个特定的字符，就增加该位置的计数器。最后如果两个列表的计数器一样，则字符串为乱序字符串。
'''
def anagramSolution3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos]+1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j+1
        else:
            stillOK = False

    return stillOK
print(anagramSolution3('aabdf','dbfaa'))
