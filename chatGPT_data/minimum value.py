def find_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
# テスト用の数値リスト
numbers = [5, 2, 9, 1, 7]
# 最小値を求める
min_value = find_min(numbers)
print("最小値:", min_value)
