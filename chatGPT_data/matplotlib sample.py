# データの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)
# グラフの描画
plt.plot(x, y)
# グラフのタイトルと軸ラベルの設定
plt.title('Sin Function')
plt.xlabel('x')
plt.ylabel('y')
# グラフの表示
plt.show()