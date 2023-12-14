# ソートする辞書
my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
# キーで辞書をソート
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
# 値で辞書をソート
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# キーと値の両方で辞書をソート
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[0], x[1])))
# ソート結果の表示
for key, value in sorted_dict.items():
    print(key, value)
