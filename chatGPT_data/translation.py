import requests
def translate_text(text, source_lang, target_lang):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "key": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    data = response.json()
    translated_text = data["data"]["translations"][0]["translatedText"]
    return translated_text
def get_user_input():
    text = input("翻訳するテキストを入力してください：")
    source_lang = input("翻訳元の言語を入力してください（例：en）：")
    target_lang = input("翻訳先の言語を入力してください（例：ja）：")
    return text, source_lang, target_lang
def main():
    text, source_lang, target_lang = get_user_input()
    translated_text = translate_text(text, source_lang, target_lang)
    print("翻訳結果：", translated_text)
main()
