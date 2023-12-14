my_dict = {"apple": "りんご", "banana": "バナナ", "orange": "オレンジ"}
# 辞書の要素の追加
my_dict["grape"] = "ぶどう"
# 辞書の要素の削除
del my_dict["banana"]
# 辞書の要素の取得
print(my_dict["apple"])
# 辞書の要素の更新
my_dict["orange"] = "みかん"
# 辞書のキーの一覧を取得
keys = my_dict.keys()
print(keys)
# 辞書の値の一覧を取得
values = my_dict.values()
print(values)
# 辞書のキーと値のペアを取得
items = my_dict.items()
print(items)
# 辞書の要素数を取得
length = len(my_dict)
print(length)
# 辞書の要素をループで処理
for key, value in my_dict.items():
    print(key, value)