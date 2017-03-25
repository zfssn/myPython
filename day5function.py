# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if a==0:
        if b==0:
            if c==0:
                return '无限解'
            else:
                return -c
        else:
            return -c/b
    else:
        k=b*b-4*a*c
        if k<0 :
            return '无解'
        else:
            k=math.sqrt(k)
        t1=(-b+k)/2/a
        t2=(-b-k)/2/a
        if t1==t2:
            return t1
        else:
            return t1,t2


a=int(input('请输入第一个参数'))
b=int(input('请输入第二个参数'))
c=int(input('请输入第三个参数'))
print('二元一次方程%sx2+%sx+%s的解为：%s' % (a,b,c,quadratic(a,b,c)))