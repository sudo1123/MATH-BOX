m=0
while m<1:
    import string
    import math
    a = int(input("��������Ҫѡ��Ĺ��ܵĴ���"))
    #����������
    if a==0:
        b = int(input("��������Ҫ���ɵ�������Χ����ע��Ҫ��һ��:"))
        def prime(b):
            number = (b)
            if number == 1:
                print(number, "��������")
                return False
            for c in range(2, int(math.sqrt(number))+1):
                if number % c == 0:
                    return False
            return True

        d = []
        for e in range(2, b):
            if prime(e):
                d.append(e)
        print("���ҵ�", len(d), "������")
        print(d)
    #��������
    if a==1:
        e = int(input("����������Ҫ��������ֵ"))
        f = int(input("����������Ҫ�����Ĵ���"))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print("������ֵΪ", j, ",���ǵ�", h, "�η���.")
    #��������ƽ����
    if a==2:
        x = float(input("��������Ҫ������ƽ����������"))
        b = 0
        z = 0
        v = z+1
        k = 1
        w = 0
        d = int(input("��Ҫ�ľ�ȷ�ȣ������������ֵԽ�߼�������С���͵�����ƽ������ֵԽ��ȷ���������ȷ���Ƿ�Ϊ���޲�ѭ��С�����Ƽ�����10000����"))
        u = []
        e = 0
        for y in range(d):
            for i in range(10):
                b = v*v
                if b < x:
                    v = v+k
                    d = d+1000
                if b > x:
                    print("�����������ƽ����������С�������ھ�ȷ����", v)
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
                print("�����������ƽ�����ǣ�", pre)
    #����Բ����
    if a == 3:
        import turtle
        myPen = turtle.Pen()
        Pos = []
        o = 0
        k = 0
        c = 0
        j = int(input("��������Ҫ�ľ��ȣ�10�ı�����"))
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
        m = float(input("�뽫��ʾ������Ϣ�к�һ����������"))
        q1=r/10000
        t = q1/m
        print("Բ����Լ����",t)
    #��n�η�
    if a==4:
        s = int(input("���������"))
        h = int(input("������ָ��"))
        o=0
        w=s
        l=h-1
        for i in range(l):
            s=s*w   
        print("�����", s)
    #��������
    if a==5:
        s = int(input("��������ѡ���ģʽ��1����ӷ�����,2�����������,3�����������,4����˷�����,5����˷����㣩"))
        if s == 1:
            b = int(input("������һ������"))
            c = int(input("��������һ������"))
            d = c+b
            print("�����", d)
        if s == 2:
            e = int(input("�����뱻����"))
            f = int(input("���������"))
            g = e-f
            print("�����", g)
        if s == 3:
            h = int(input("�����뱻����"))
            j = int(input("���������"))
            if j == 0:
                print("������ĳ�����0��0������Ϊ����")
            else:
                k = h/j
                print("�����", k)
        if s == 4:
            l = int(input("������һ������"))
            m = int(input("��������һ������"))
            n = l*m
            print("�����", n)
        if s == 5:
            o = int(input("���������"))
            p = int(input("������ָ��"))
            for q in range(p):
                r = o*o
            print("�����", r)
    #����쳲���������
    if a == 6:
        a = (int(input("�����뷶Χ")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        print(d)
    #����ƽ�ָ���
    if a == 7:
        a = (int(input("�����뷶Χ")))
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
        print("�ƽ�ָ���ԼΪ",v)
#��ֹ����
    if a == 1001:
        m=2