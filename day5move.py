# -*- coding: utf-8 -*-
B=[]
def move(n,a,b,c):

    if n==1 :
        buzhou=a+'-->'+c
        B.append(buzhou)
        return
    buzhou=a+'-->'+c
    B.append(buzhou)
     

move(1,'A','B','C')
for b in B:
    print(b)