# 問題1: リストの要素を合計する
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# 問題2: タプルの要素を逆順にする
def reverse_tuple(t):
    return tuple(reversed(t))
# 問題3: 辞書のキーと値を入れ替える
def swap_dict(d):
    return {value: key for key, value in d.items()}
# 問題4: 集合の要素をリストに変換する
def set_to_list(s):
    return list(s)
# 問題5: 文字列の中で最も出現回数の多い文字を返す
def most_common_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_count = max(char_count.values())
    most_common_chars = [char for char, count in char_count.items() if count == max_count]
    return most_common_chars
# テストデータ
numbers = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
d = {'apple': 'りんご', 'banana': 'バナナ', 'orange': 'オレンジ'}
s = {1, 2, 3, 4, 5}
string = "abracadabra"
# テスト実行
print("問題1: リストの要素を合計する")
print("入力:", numbers)
print("出力:", sum_list(numbers))
print()
print("問題2: タプルの要素を逆順にする")
print("入力:", t)
print("出力:", reverse_tuple(t))
print()
print("問題3: 辞書のキーと値を入れ替える")
print("入力:", d)
print("出力:", swap_dict(d))
print()
print("問題4: 集合の要素をリストに変換する")
print("入力:", s)
print("出力:", set_to_list(s))
print()
print("問題5: 文字列の中で最も出現回数の多い文字を返す")
print("入力:", string)
print("出力:", most_common_char(string))
