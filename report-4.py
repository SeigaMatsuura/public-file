import csv
from math import atan, atan2, cos, pi, sin, sqrt, tan
import numpy as np

e = 0.75
a = 26610
i = -63.4*pi/180 #軌道傾斜角
Ω = -45*pi/180 #昇交点赤経
w = -270*pi/180 #近点引数

#行列の定義
arri = np.matrix([[1,       0,      0], 
                  [0,  cos(i), sin(i)],
                  [0, -sin(i), cos(i)]])

arrΩ = np.matrix([[cos(Ω), sin(Ω), 0], 
                 [-sin(Ω), cos(Ω), 0],
                 [      0,      0, 1]])

arrw = np.matrix([[cos(w), sin(w), 0], 
                 [-sin(w), cos(w), 0],
                 [      0,      0, 1]])

def fx(x,M):
    return x - e*sin(x) - M

def dfx(x):
    return 1 - e*cos(x)

epsilon1=0.000001

# CSVファイルを作成⇨書き込む
with open('report4.csv', 'w') as csv_file:
    fieldnames = ['t-t0', 'Rx[km]', 'Ry[km]', 'Rz[km]', 'Vx[km/s]', 'Vy[km/s]', 'Vz[km/s]']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(25):
        T = 30*i
        M = 15*i
        
        M1 = M*pi/180
        E = 400
        while True:
            E1 = E - fx(E,M1)/dfx(E)

            if abs(fx(E1,M1)-fx(E,M1)) < epsilon1:
                E = E1
                E2 = E*180/pi
                break 

            E = E1

        f1 = atan2(((cos(E)-e)/(1-e*cos(E))),(sqrt(1-e**2)*sin(E))/(1-e*cos(E)))
        f = 90 - f1*180/pi
        f2 = f*pi/180

        r = a*(1-e**2)/(1+e*cos(f2))
        R = np.array([r*cos(f2), r*sin(f2), 0])
        R = R.T

        v = (2*pi/720)*a*sqrt((1+e**2+2*e*cos(f2))/(1-e**2))/60
        V = np.array([v*cos(f2), v*sin(f2), 0])
        V = V.T

        R1 = np.dot(arrw,R)
        R1 = R1.T
        R1 = np.dot(arri,R1)
        R1 = np.dot(arrΩ,R1)
        R1T = R1.T

        phai = atan(e*sin(f2)/(1+e*cos(f2)))
        PHAI = np.array([sin(phai-f2), cos(phai-f2), 0])

        G1 = np.dot(arrw,PHAI)
        G1T = G1.T
        G2 = np.dot(arri,G1T)
        G3 = np.dot(arrΩ,G2)
        V1 = v * G3
        V1T = V1.T
    
        writer.writerow({'t-t0': T, 'Rx[km]':R1T[0,0], 'Ry[km]':R1T[0,1], 'Rz[km]':R1T[0,2], 'Vx[km/s]':V1T[0,0], 'Vy[km/s]':V1T[0,1], 'Vz[km/s]':V1T[0,2]})