import random
def generate_target():
    return random.randint(1, 10)
def get_user_guess():
    while True:
        try:
            user_guess = int(input("1から10までの数字を予想してください："))
            if 1 <= user_guess <= 10:
                return user_guess
            else:
                print("無効な数字です。もう一度入力してください。
        except ValueError:
            print("無効な入力です。数字を入力してください。
def play_game():
    target = generate_target()
    print("的あてゲームを始めます！")
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        if user_guess == target:
            print("正解です！")
            print("試行回数：", attempts)
            break
        elif user_guess < target:
            print("もっと大きい数字です。
        else:
            print("もっと小さい数字です。
play_game()
