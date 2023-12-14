def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
# テスト用の数値リスト
numbers = [5, 2, 9, 1, 7]
# 最大値を求める
max_value = find_max(numbers)
print("最大値:", max_value)
