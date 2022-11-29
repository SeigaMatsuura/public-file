import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, sqrt


while True:
    for RS in range(1,10, 1):
        R = np.linspace(0, 100000)
        RSb = RS/5

        dv =  ((1+R)/2)**(3/2)
        dv2 = ((1+RSb)/2)**(3/2) + ((RSb+R)/2)**(3/2)
        dv2 = dv2 - dv


        plt.plot(R, dv2, color='blue', ls='-', label=RSb)

        plt.xlim(0, 100)
        plt.ylim(-5, 10)

        plt.legend()
        plt.xlabel('R')
        plt.ylabel('Δv')
        plt.title('Transfer')

        plt.draw()
        plt.pause(1) # SleepTime時間だけ表示を継続
        plt.clf() # プロットした点を消してグラフを初期化