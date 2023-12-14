import random
def get_user_choice():
    while True:
        user_choice = input("じゃんけんの手を入力してください（グー、チョキ、パー）：")
        if user_choice in ["グー", "チョキ", "パー"]:
            return user_choice
        else:
            print("無効な手です。もう一度入力してください。
def get_computer_choice():
    choices = ["グー", "チョキ", "パー"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == "グー" and computer_choice == "チョキ") or \\
         (user_choice == "チョキ" and computer_choice == "パー") or \\
         (user_choice == "パー" and computer_choice == "グー"):
        return "ユーザーの勝ち"
    else:
        return "コンピューターの勝ち"
def play_game():
    print("じゃんけんを始めます！")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("ユーザーの選択：", user_choice)
    print("コンピューターの選択：", computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    print("結果：", winner)
play_game()
