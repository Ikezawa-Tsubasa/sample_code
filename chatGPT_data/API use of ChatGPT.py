import openai
import time
# OpenAI APIの設定
openai.api_key = "YOUR_API_KEY"
model_engine = "davinci"  # 使用するモデルのエンジン
# 対話を開始する
def start_chat():
    print("こんにちは！私はChatGPTです。")
    while True:
        user_input = input("あなた：")
        if user_input.lower() in ["さようなら", "終了", "おわり"]:
            print("ChatGPT：さようなら！またお話しましょう！")
            break
        response = get_response(user_input)
        print("ChatGPT：" + response)
        time.sleep(1)
# OpenAI APIを使用して、応答を取得する
def get_response(user_input):
    prompt = "User: " + user_input + "\
ChatGPT:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
if __name__ == "__main__":
    start_chat()
