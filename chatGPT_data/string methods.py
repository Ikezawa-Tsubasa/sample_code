def count_characters(text):
    return len(text)
def capitalize_text(text):
    return text.capitalize()
def reverse_text(text):
    return text[::-1]
def check_palindrome(text):
    reversed_text = reverse_text(text)
    if text.lower() == reversed_text.lower():
        return True
    else:
        return False
def main():
    text = input("テキストを入力してください：")
    print("文字数：", count_characters(text))
    print("先頭を大文字にしたテキスト：", capitalize_text(text))
    print("逆順のテキスト：", reverse_text(text))
    if check_palindrome(text):
        print("回文です。
    else:
        print("回文ではありません。
main()
