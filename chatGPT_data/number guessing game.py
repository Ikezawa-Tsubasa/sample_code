import random
def game():
    number = random.randint(1, 100)
    attempts = 0
    print("数当てゲームを開始します！")
    print("1から100までの数を当ててください。")
    while True:
        guess = int(input("予想した数を入力してください: "))
        attempts += 1
        if guess < number:
            print("もっと大きい数です。")
        elif guess > number:
            print("もっと小さい数です。")
        else:
            print("正解です！")
            print("あなたは{}回で正解しました。".format(attempts))
            break
game()
