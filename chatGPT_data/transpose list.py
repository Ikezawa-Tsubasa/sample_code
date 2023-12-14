# 転置するリスト
my_list = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
# 転置したリストを格納する変数
transposed_list = []
# 転置を行う
for i in range(len(my_list[0])):
    transposed_row = []
    for row in my_list:
        transposed_row.append(row[i])
    transposed_list.append(transposed_row)
# 転置結果の表示
for row in transposed_list:
    print(row)
