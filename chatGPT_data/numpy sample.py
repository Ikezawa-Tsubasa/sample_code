a = np.array([1, 2, 3, 4, 5])
print(a)
# 2次元配列の作成
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# 配列の形状の取得
print(a.shape)
print(b.shape)
# 配列の要素数の取得
print(a.size)
print(b.size)
# 配列のデータ型の取得
print(a.dtype)
print(b.dtype)
# 配列の要素へのアクセス
print(a[0])
print(b[1, 2])
# 配列のスライシング
print(a[1:4])
print(b[:, 1:])
# 配列の演算
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(c + d)
print(c * d)
print(np.dot(c, d))
# 配列の統計処理
e = np.array([1, 2, 3, 4, 5])
print(np.sum(e))
print(np.mean(e))
print(np.max(e))
print(np.min(e))
# 配列の変形
f = np.array([[1, 2, 3], [4, 5, 6]])
print(f.reshape(3, 2))
# 配列の転置
print(f.T)
# 配列の結合
g = np.array([1, 2, 3])
h = np.array([4, 5, 6])
print(np.concatenate([g, h]))
print(np.vstack([g, h]))
print(np.hstack([g, h]))