try:
    num1 = int(input("最初の数を入力してください: "))
    num2 = int(input("次の数を入力してください: "))
    result = num1 / num2
    print("結果:", result)
except ValueError:
    print("入力された値が正しくありません。整数を入力してください。
except ZeroDivisionError:
    print("0で割ることはできません。別の数を入力してください。
except Exception as e:
    print("予期せぬエラーが発生しました:", e)
