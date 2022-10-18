import numpy as np

# ax^4 + bx^3 + cx^2 + dx +e = M


a = 5.67*10**(-8)
b = 0
c = 0
d = 2.3
e = -288*2.3-(5.67*(288**4))*(10**(-8))

M = 600

'''
a = 0
b = 0
c = 1
d = 0
e = 0

M = 1.1
'''

x = 1000
epsilon1=0.01
n = 0

def f(x):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e - M

def df(x):
    return 4*a*x**3 + 3*b*x**2 + 2*c*x +d

while True:
    x1 = x - f(x)/df(x)
    n += 1
    if abs(f(x1)-f(x)) < epsilon1:
        x = x1
        break 

    x = x1

print(x,n)