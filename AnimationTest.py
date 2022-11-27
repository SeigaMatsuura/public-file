# ２次元リアルタイムグラフの雛形

# Library
import numpy as np # プロットするデータ配列を作成するため
import matplotlib.pyplot as plt # グラフ作成のため
import random

# params
a = []
b = []
p = []
q = []
sleepTime = 0.1  # １フレーム表示する時間[s]
i = 0
P = 130
Q = 33
fig = plt.figure()
PHASE = 0

press = fig.add_subplot(2, 2, 1)
gps = fig.add_subplot(2, 2, 2)

# plotting
while True:

    press = fig.add_subplot(2, 2, 1)
    gps = fig.add_subplot(2, 2, 2)

    i = i + 1 # フレーム回数分グラフを更新
    x = 1023 - i - random.uniform(0,10)
    a.append(x)# プロットするデータを作成
    b.append(i)

    P = P + random.uniform(0,1)
    Q = Q + random.uniform(0,1)
    p.append(P)
    q.append(Q)
    
    fig.text(0.1, 0.35, "PRESSURE")
    fig.text(0.1, 0.3, x)
    fig.text(0.1, 0.25, "TIME")
    fig.text(0.1, 0.2, i * 0.5)
    fig.text(0.6, 0.35, "LON")
    fig.text(0.6, 0.3, P)
    fig.text(0.6, 0.25, "LAT")
    fig.text(0.6, 0.2, Q)
    fig.text(0.3, 0.25, "PHASE")
    fig.text(0.3, 0.2, PHASE)

    # plt.plot(b,a) # データをプロット
    press.plot(a, color="blue")
    gps.plot(p,q, color="blue")
    plt.draw() # グラフを画面に表示開始
    plt.pause(sleepTime) # SleepTime時間だけ表示を継続
    plt.clf() # プロットした点を消してグラフを初期化