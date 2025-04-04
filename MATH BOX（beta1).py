import math
a = int(input(000))
#生成质数表
if a==0:
    b = int(input("请输入您要生成的质数表范围：（注意要加一）:"))
    def prime(b):
        number = (b)
        if number == 1:
            print(number, "不是质数")
            return False
        for c in range(2, int(math.sqrt(number))+1):
            if number % c == 0:
                return False
        return True

    d = []
    for e in range(2, b):
        if prime(e):
            d.append(e)
    print("共找到", len(d), "个质数")
    print(d)
#翻倍运算
if a==1:
    e = int(input("请输入您需要翻倍的数值"))
    f = int(input("请输入您需要翻倍的次数"))
    j = 0
    h = 0
    for i in range(f):
        j= e*2
        h += 1
        e = j
        print("现在数值为", j, ",这是第", h, "次翻倍.")
#计算算数平方根
x = float(input("请输入需要求算术平方根的数："))
b = 0
z = 0
v = z+1
k = 1
w = 0
d = int(input("需要的精确度（输入的整数数值越高计算无限小数型的算术平方根数值越精确，如果不能确定是否为无限不循环小数，推荐输入10000）："))
u = []
e = 0
for y in range(d):
    for i in range(10):
        b = v*v
        if b < x:
            v = v+k
            d = d+1000
        if b > x:
            print("这个数的算术平方根是无限小数，现在精确到：", v)
            w = v
            v = v/10
            k = k/10
        if b == x:
            u.append(v)
            e = len(u)
            for q in range(e-1):
                 u.pop()
if u == []:
    print("这个数的算术平方根是无限小数", u)
else:
    print("这个数的算术平方根是：", u)
