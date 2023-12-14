import random
def generate_target():
    # 1から100までのランダムな数を生成して返す
    return random.randint(1, 100)
def play_game():
    target = generate_target()
    attempts = 0
    while True:
        guess = int(input("1から100までの数を予想してください: "))
        attempts += 1
        if guess < target:
            print("もっと大きい数です")
        elif guess > target:
            print("もっと小さい数です")
        else:
            print("正解です！")
            break
    print("正解までに{}回の予想が必要でした".format(attempts))
play_game()
