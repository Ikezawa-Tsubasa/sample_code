import requests
def check_spelling(text):
    url = "https://api.textgears.com/spelling"
    params = {
        "text": text,
        "language": "en",
        "key": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    data = response.json()
    errors = data["response"]["errors"]
    suggestions = []
    for error in errors:
        suggestions.append(error["better"])
    return suggestions
def get_user_input():
    text = input("スペルチェックするテキストを入力してください：")
    return text
def main():
    text = get_user_input()
    suggestions = check_spelling(text)
    if len(suggestions) > 0:
        print("スペルミスが見つかりました。
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("スペルミスは見つかりませんでした。
main()
