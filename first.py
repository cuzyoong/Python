# -*- coding: utf-8 -*-
'''
sum=0
for x in range(101):
    sum=sum+x
print(sum)
#==
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
#==
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello'+' '+x)
#==
n=1
while n<100:
    if n>10:
        break
    print(n)
    n=n+1
print('end')
#==
n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
#==
d={'Mac':95,'Bob':98,'Tracy':87}
print(d['Bob'])
#==
print(hex(255))

import math
def quadratic(a,b,c):
    t = b*b-4*a*c
    if(t >0):
        x1=(-b+math.sqrt(t))/(2*a)
        x2=(-b-math.sqrt(t))/(2*a)
        return x1,x2
    elif(t==0):
        x=-b/(2*a)
        return x
    else:
        return'none result'
print(quadratic(1,3,-4))

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(2,3))

def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)
move(2,'a','b','c')

L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print(L)
print(L[3:5])#切片

R=[x*x for x in range(1,11)]#括号右边不取
print(R)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str) ]
print(L2)

def normalize(name):
    return name[0].upper()+name[1::].lower()
L1=['adam', 'LISA', 'barT']
L2=list(map(normalize,L1))
print(L2)

from functools import reduce
L1=[3, 5, 7, 9]
def mult(x,y):
    return x*y
def prod(L):
    return reduce(mult,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
'''
from functools import reduce
def str2float(s):
    return reduce(lambda x,y: x + (y / (10 ** len(str(y)))) ,list(map(lambda x:int(x),s.split('.'))))
