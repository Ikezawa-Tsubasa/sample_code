def uppercase_decorator(func):
    def wrapper():
        # 元の関数を実行し、結果を取得
        result = func()
        # 結果を大文字に変換して返す
        return result.upper()
    return wrapper
@uppercase_decorator
def say_hello():
    return "hello"
# デコレータを適用した関数を呼び出し
print(say_hello())
