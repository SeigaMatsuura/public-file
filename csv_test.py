import csv
from math import atan, atan2, cos, pi, sin, sqrt, tan

e = 0.75
a = 26610

def fx(x,M):
    return x - e*sin(x) - M

def dfx(x):
    return 1 - e*cos(x)

epsilon1=0.01

# CSVファイルを作成⇨書き込む
with open('orbit20.csv', 'w') as csv_file:
    fieldnames = ['t-t0', 'M[deg]', 'E[Deg]', 'f[Deg]', 'r[km]', 'v[km/s]', 'φ[deg]']
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

        v = (2*pi/720)*a*sqrt((1+e**2+2*e*cos(f2))/(1-e**2))/60

        phai = atan(e*sin(f2)/(1+e*cos(f2)))*180/pi


        writer.writerow({'t-t0': T, 'M[deg]': M, 'E[Deg]':E2, 'f[Deg]':f, 'r[km]':r, 'v[km/s]':v, 'φ[deg]':phai})

