import csv
import numpy as np
import math 

# 位置を指定
r = np.array([5492.00034, 3984.00140, 2.95581])
R = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)

# 速度を指定
v = np.array([-3.931046491, 5.498676921, 3.665980697])
V = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

# North Porl 方向の単位ベクトルの指定
I = np.array([1, 0, 0])
J = np.array([0, 1, 0])
K = np.array([0, 0, 1])

# 地心重力定数の指定
μ = 398600.5

h = np.cross(r,v) #角運動量の決定
H = math.sqrt(h[0]**2 + h[1]**2 + h[2]**2)
print(h)

n = np.cross(K,h) #node vectorの決定
N = math.sqrt(n[0]**2 + n[1]**2 + n[2]**2)
print(n)

e = -(np.cross(h,v)/μ) - r/R #離心率ベクトルの決定
E = math.sqrt(e[0]**2 + e[1]**2 + e[2]**2)
print(e) 

a = (2/R - (V**2)/μ)**(-1) #長半径の決定
print(a)

khh = np.dot(K,h)/H #傾斜角の決定
i = math.acos(khh)
print(i*180/math.pi)

cΩ = math.acos(np.dot(n,I)/N) #昇交点赤経の決定
sΩ = math.asin(np.dot(n,J)/N)
if sΩ<0:
    Ω = 2*math.pi - math.acos(np.dot(n,I)/N)
else:
    Ω = math.acos(np.dot(n,I)/N)
print(Ω*180/math.pi)

if e[2]<0: #近点引数の決定
    w = 2*math.pi - math.acos(np.dot(n,e)/(N*E))
else:
    w = math.acos(np.dot(n,e))/(N*E)
print(w*180/math.pi)

rv = np.dot(r,e) #真近点離角
if rv<0:
    f = 2*math.pi - math.acos(np.dot(r,e)/(R*E))
else:
    f = math.acos(np.dot(r,e)/(R*E))
print(f*180/math.pi)


#ここからは追加課題
#緯度引数uを求める
if r[2]<0:
    u = 2*math.pi - math.acos(np.dot(r,n)/(R*N))
else:
    u = math.acos(np.dot(r,n)/(R*N))
print(u*180/math.pi)

#離心近点点離角を求める
cEc = (E + math.cos(f))/(1 + E*math.cos(f))
sEc = (math.sqrt(1 - E**2)*math.sin(f))/(1 + E*math.cos(f))
if sEc < 0:
    Ec = 2*math.pi - math.acos(cEc)
else:
    Ec = math.acos(cEc)
print(Ec*180/math.pi)

#平均近点離角を求める
M = Ec - E*math.sin(Ec)
print(M)

#経路角を求める
φ = math.atan(E*math.sin(f)/math.sqrt(1-E**2))
print(φ*180/math.pi)

#周期を求める
P = math.pi*a*a*math.sqrt(1-E**2)/((1/2)*R*V*math.cos(φ))
print(P)
