# ラムダ式を使用して2つの数値を足す関数を定義
add = lambda x, y: x + y
# ラムダ式を使用して2つの数値を掛ける関数を定義
multiply = lambda x, y: x * y
# テスト用の数値
a = 5
b = 3
# ラムダ式を使用して2つの数値を足す
result_add = add(a, b)
print("足し算の結果:", result_add)
# ラムダ式を使用して2つの数値を掛ける
result_multiply = multiply(a, b)
print("掛け算の結果:", result_multiply)
