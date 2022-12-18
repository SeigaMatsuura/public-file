from math import atan, atan2, cos, pi, sin, sqrt, tan
import matplotlib.pyplot as plt
import numpy as np

Vmin = 73.5
Vmax = 340 * 0.85
Cd0 = 0.02
e = 0.8
M = 219540
S = 325
b = 60.1
AR = (b**2)/S
r = 1.225
g = 9.8
FW = 10


fig, ax = plt.subplots()
v = np.linspace(Vmin,Vmax,100000)
ax.set_xlim(0, 800)
ax.set_ylim(0, 20)


Cl = (2*M*g)/(r*S*v**2)
Cd = Cd0 + (Cl**2)/(np.pi*AR*e)


gamma = np.arctan2(Cd,Cl)
'''
w = (v**2)*e*S*Cl/(2*1000000*np.cos(r))
'''

v2 = (2*M*g*np.cos(gamma)/(e*S*Cl))**(1/2)
w = v2 * np.sin(gamma)
v = v2* np.cos(gamma) - FW
ax.invert_yaxis()
ax.plot(v*3.6,w)


for i in range(1000):
    va = Vmin + (Vmax-Vmin)*i/1000
    vb = Vmin + (Vmax-Vmin)*(i+1)/1000
    Cl2 = (2*M*g)/(r*S*va**2)
    Cd2 = Cd0 + (Cl2**2)/(np.pi*AR*e)
    Cl3 = (2*M*g)/(r*S*vb**2)
    Cd3 = Cd0 + (Cl3**2)/(np.pi*AR*e)

    gamma2 = np.arctan2(Cd2,Cl2)
    gamma3 = np.arctan2(Cd3,Cl3)

    dy = ((2*M*g*np.cos(gamma3)/(e*S*Cl3))**(1/2))*np.sin(gamma3) - ((2*M*g*np.cos(gamma2)/(e*S*Cl2))**(1/2))*np.sin(gamma2)
    dx = ((2*M*g*np.cos(gamma3)/(e*S*Cl3))**(1/2))*np.cos(gamma3) - ((2*M*g*np.cos(gamma2)/(e*S*Cl2))**(1/2))*np.cos(gamma2)

    dl = dy/dx

    y = dl*(FW-(2*M*g*np.cos(gamma2)/(e*S*Cl2))**(1/2)*np.cos(gamma2)) + ((2*M*g*np.cos(gamma2)/(e*S*Cl2))**(1/2))*np.sin(gamma2)
    if abs(y) <= 0.1:
        break
print((FW-(2*M*g*np.cos(gamma2)/(e*S*Cl2))**(1/2)*np.cos(gamma2))*3.6, 1/np.tan(gamma2), np.arctan(dl)*180/np.pi)


p = np.linspace(0,Vmax,100000)
ax.plot(3.6*(p),dl*p)
plt.show()
