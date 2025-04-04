j1=0
#保存函数（存在程序所在处）
import json
with open("number saved.json","r") as jj:
    tt=json.load(jj)
def saved(quqi,p):
    c=str(input("您是否要保存结果？（是按1，不是按2）"))
    if c=="1":
        ww=[]
        if tt=="0":
            with open("reply.json","w") as z:
                json.dump("*",z)
            with open("number saved.json","w") as zz:
                json.dump("1",zz)
        with open("reply.json","r") as g:
            ee=json.load(g)
            ww.append(ee)
            ww.append(quqi)
            ww.append(p)
        with open("reply.json","w") as f:
            json.dump(ww,f)
        print("完成，已存至reply.json")
    if c=="2":
        z=1
def history(quqi):
    ww=[]
    with open("history.json","r") as g:
        ee=json.load(g)
        ww.append(ee)
        ww.append(quqi)
    with open("history.json","w") as f:
        json.dump(ww,f)
def save(quqi,w14):
    ww=[]
    with open("reply.json","w") as z:
        json.dump("*",z)
    with open("number saved.json","w") as zz:
        json.dump("1",zz)
    with open("reply.json","r") as g:
        ee=json.load(g)
        ww.append(ee)
        ww.append(quqi)
        ww.append(w14)
    with open("reply.json","w") as f:
        json.dump(w14,f)    
history("turn on*")
print("hello")
#前端        
while True:
    import string
    import math
    if j1>0:
        a = input("请输入需要选择的功能的代码(输入shutdown关闭程序，输入help查看使用指南)")
    else:
        a = input("请输入需要选择的功能的代码(0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率,8是找零程序（贪心算法），9是统计，输入shutdown关闭程序，输入help查看使用指南")
        j1+=1
    #生成质数表
    if a=="0":
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
        saved("the reply from fuction 0",d)
        history("0*")
    #翻倍运算
    if a=="1":
        e = int(input("请输入您需要翻倍的数值"))
        f = int(input("请输入您需要翻倍的次数"))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print("现在数值为", j, ",这是第", h, "次翻倍.")
            w=j
        saved("the reply from fuction 1",w)
        history("1*")
    #计算算数平方根
    if a=="2":
        x = float(input("请输入需要求算术平方根的数："))
        b = 0
        z = 0
        v = z+1
        k = 1
        w = 0
        d = int(input("需要的精确度（输入的整数数值越高计算无限小数型的算术平方根数值越精确，如果不能确定是否为无限不循环小数，推荐输入10000）："))
        u = []
        e = 0
        pre=0
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
                w22=90
            else:
                pre = u[0]
                print("这个数的算术平方根是：", pre)
        saved("the reply from fuction 2",pre)
        saved("genhao",x)
        history("2*")
    #计算圆周率
    if a =="3":
        c=int(input("请选择使用代数法还是几何法（代数法按1，几何法按2）"))
        if c==1:#代数法
            a=0
            b=1
            d=0
            e=int(input("请输入您需要的范围（10的倍数）"))
            for c in range(1,e):
                d=2*c-1
                if b==1:
                    a+=1/d
                else:
                    a-=1/d
                print("圆周率约等于",4*a)
                b=b*-1
                d=4*a
            saved("the reply from fuction 3",d)
            history("3(1)*")
        if c==2:#几何法
            import turtle
            myPen = turtle.Pen()
            Pos = []
            o = 0
            k = 0
            c = 0
            j = int(input("请输入需要的精度（10的倍数）"))
            r = 360*j
            py = r/2
            myPen.speed(0)
            for i in range(int(py)):
                print(i+1)
                myPen.forward(0.0001)
                myPen.left(1/j)
                o = o+1
                if o == r/2:
                    Pos.append(myPen.pos())
            print(Pos)
            m = float(input("请将显示的是信息中后一个数字输入"))
            q1=r/10000
            t = q1/m
            print("圆周率约等于",t)
            saved("the reply from fuction 3",t)
            history("3(2)*")
    #求n次方
    if a=="4":
        s = int(input("请输入底数"))
        h = int(input("请输入指数"))
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            s=s*w   
        print("结果是", s)
        saved("the reply from fuction 4",s)
        ll=ll+1
        save("^",h)
        save("=",s)
        history("4*")
    #四则运算
    if a=="5":
        s = int(input("请输入您选择的模式（1代表加法运算,2代表减法运算,3代表除法运算,4代表乘法运算）"))
        if s == 1:
            b = int(input("请输入一个加数"))
            c = int(input("请输入另一个加数"))
            d = c+b
            print("结果是", d)
            ee=0
            saved("the reply from fuction 5[1]",b)
            ee=ee+1
            save("+",c)
            save("=",d)
            ee=0
            history("5(1)*")
        if s == 2:
            e = int(input("请输入被减数"))
            f = int(input("请输入减数"))
            g = e-f
            print("结果是", g)
            ff=0
            saved("the reply from fuction 5[2]",e)
            ff=ff+1
            save("-",f)
            save("=",g)
            ff=0
            history("5(2)*")
        if s == 3:
            h = int(input("请输入被除数"))
            j = int(input("请输入除数"))
            if j == 0:
                print("您输入的除数是0，0不能作为除数")
            else:
                k = h/j
                print("结果是", k)
            jj=0
            saved("the reply from fuction 5[3]",h)
            jj=jj+1
            save("/",j)
            save("=",k)
            jj=0
            history("5(3)*")
        if s == 4:
            l = int(input("请输入一个乘数"))
            m = int(input("请输入另一个乘数"))
            n = l*m
            print("结果是", n)
            gg=0
            saved("the reply from fuction 5[4]",l)
            gg=gg+1
            save("*",m)
            save("=",n)
            history("5(4)*")
    #生成斐波那契数列
    if a =="6":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        print(d)
        saved("the reply from fuction 6",d)
        history("6*")
    #计算黄金分割率
    if a =="7":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        s=len(d)
        v=d[s-2]/d[s-1]
        print("黄金分割率约为",v)
        saved("the reply from fuction 7",v)
        history("7*")
    if a=="8":
        target= Input=float(input("请输入您需要找的钱数：（人民币）"))
        money=[100,50,20,10,5,1,0.5,0.1]
        number=[0,0,0,0,0,0,0,0,0]
        saved1=[]

        for i in range(8):
            number[i]=target//money[i]
            target=target%money[i]
        for i in range(8):
            print(money[i],"元的张数为",number[i],"张")
            saved1.append(money[i])
            saved1.append(number[i])
        saved("the reply from fuction 8",saved1)
        history("8*")
    if a=="9":
        b=int(input("输入1求平均值，输入2求加权平均值，输入3求方差，输入4求标准差"))
        if b==1:
            c=[]
            d=[]
            f=2
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    f=0
                    c.pop()
            for i in range(len(c)):
                d.append(float(c[i]))
            w1=0
            w2=0
            for w3 in range(len(d)):
                w1=d[i]
                w2=w2+w1
            w4=w2/len(d)
            print(d,"的平均值为",w4)
            saved("the reply from fuction9(1)",w4)
            history("9(1)*")
        if b==2:
            c=[]
            d=[]
            f=2
            o=2
            w1=[]
            w4=[]
            w6=[]
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    c.pop()
                    f=0
            while 0<o:
                w2=input("请输入权（一次一个，输入完毕输f)")
                w1.append(w2)
                if w2=="f":
                    w1.pop()
                    o=0
            for w3 in range(len(c)):
                w4.append(float(w1[w3]))
            for w5 in range(len(w1)):
                w6.append(float(w1[w5]))
            w11=0
            w12=0
            w14=0
            for w7 in range(len(w1)):
                w8=w4[w7]
                w9=w6[w7]
                w10=w8*w9
                w11=w11+w10
                w12=w12+w9
                w14=w11/w12
            print("加权平均数为",w14)
            saved("the reply from fuction9(2)",w14)
            history("9(2)*")
        if b==3:
             c=[]
             d=[]
             f=2
             while 0<f:
                 e=input("请输入数据（一次一个，输入完毕输f)")
                 c.append(e)
                 if e=="f":
                     f=0
                     c.pop()
             for i in range(len(c)):
                 d.append(float(c[i]))
             w1=0
             w2=0
             for w3 in range(len(d)):
                 w1=d[i]
                 w2=w2+w1
             w4=w2/len(d)
             w6=0
             for w7 in range(len(d)):
                 w8=d[w7]-w4
                 w8=w8*w8
                 w6=w6+w8
             w9=w6/len(d)
             print("方差为",w9)
             saved("the reply from fuction9(3)",w9)
             history("9(3)*")
        if b==4:
            c=[]
            d=[]
            f=2
            while 0<f:
                e=input("请输入数据（一次一个，输入完毕输f)")
                c.append(e)
                if e=="f":
                    f=0
                    c.pop()
            for i in range(len(c)):
                d.append(float(c[i]))
            w1=0
            w2=0
            for w3 in range(len(d)):
                w1=d[w3]
                w2=w2+w1
            w4=w2/len(d)
            w6=0
            for w7 in range(len(d)):
                w8=d[w7]-w4
                w8=w8*w8
                w6=w6+w8
            w9=w6/len(d)
            x = w9
            b = 0
            z = 0
            v = z+1
            k = 1
            w = 0
            d = int(input("需要的精确度（输入的整数数值,越高计算越精确"))
            u = []
            e = 0
            pre=0
            for y in range(d):
                for i in range(10):
                    b = v*v
                    if b < x:
                        v = v+k
                        d = d+1000
                    if b > x:
                        print("标准差是无限小数，现在精确到：", v)
                        w = v
                        v = v/10
                        k = k/10
                    if b == x:
                        u.append(v)
                        e = len(u)
                        for q in range(e-1):
                            u.pop()
                if u == []:
                    print()
                else:
                    pre = u[0]
                    print("标准差是", pre)
            saved("the reply from fuction9(4)",pre)
            history("9(4)")
#帮助
    if a=="help":
        print("请输入需要选择的功能的代码(0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率,8是找零程序（贪心算法），9是统计，输入shutdown关闭程序，输入help查看使用指南")
#终止运行
    if a =="shutdown":
        break
        history("turn off")
#调试
    if a=="special":
        q1=input("输入密钥")
        with open("miyao.json","r") as jj:
            tt=json.load(jj)
        if tt==q1:
            with open("history.json","r") as yy:
                o1=json.load(yy)
            print(o1)
        else:
            print("密钥错误")
print("再见")
print("hope to see you again")
