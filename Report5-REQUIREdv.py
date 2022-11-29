import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, sqrt



for RS in range(1,10000, 1):
    R = np.linspace(0, 100)
    RSb = RS/5
    # RSx = 100
    # RSy = 15
    # RSz = 5

    dv =  ((2*R/(1+R))**(1/2)-1) + (1/R**(1/2))*(1-(2/(1+R))**(1/2))
    dv2 = ((2*RSb/(1+RSb))**(1/2)-1) + ((2/RSb)**(1/2))*(((R/(R+RSb))**(1/2))-((1/(1+RSb))**(1/2))) + abs((1/R**(1/2))*((2*RSb/(RSb+R))**(1/2)-1))
    # dvx = ((2*RSx/(1+RSx))**(1/2)-1) + ((2/RSx)**(1/2))*(((R/(R+RSx))**(1/2))-((1/(1+RSx))**(1/2))) + (1/R**(1/2))*((2*RSx/(RSx+R))**(1/2)-1)
    # dvy = ((2*RSy/(1+RSy))**(1/2)-1) + ((2/RSy)**(1/2))*(((R/(R+RSy))**(1/2))-((1/(1+RSy))**(1/2))) + (1/R**(1/2))*((2*RSy/(RSy+R))**(1/2)-1)
    # dvz = ((2*RSz/(1+RSz))**(1/2)-1) + ((2/RSz)**(1/2))*(((R/(R+RSz))**(1/2))-((1/(1+RSz))**(1/2))) + (1/R**(1/2))*((2*RSz/(RSz+R))**(1/2)-1)

    plt.plot(R, dv, color='red', ls='-', label='Hohmann')
    plt.plot(R, dv2, color='blue', ls='-', label=RSb)
    # plt.plot(R, dvx, color='palegreen', ls='-', label='Hohmann')
    # plt.plot(R, dvy, color='darkgreen', ls='-', label='Hohmann')
    # plt.plot(R, dvz, color='blue', ls='-', label='Hohmann')
    # if 13<RSb<18:
    #     plt.xlim(0, 30)
    #     plt.ylim(0.4, 0.6)
    # else:
    plt.xlim(0, 60)
    plt.ylim(0.4, 0.7)

    plt.legend()
    plt.xlabel('R')
    plt.ylabel('Δv')
    plt.title('Transfer')

    plt.draw()
    plt.pause(0.1) # SleepTime時間だけ表示を継続
    plt.clf() # プロットした点を消してグラフを初期化