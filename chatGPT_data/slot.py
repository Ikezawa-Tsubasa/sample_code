import random
# スロットのリールに表示されるシンボル
symbols = ["7", "BAR", "BELL", "CHERRY", "LEMON"]
# スロットのリールを回す関数
def spin():
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)
    return [reel1, reel2, reel3]
# スロットのリールを表示する関数
def display(reels):
    print("-------------")
    print("| {} | {} | {} |".format(reels[0], reels[1], reels[2]))
    print("-------------")
# スロットの結果を判定する関数
def judge(reels):
    if reels[0] == reels[1] == reels[2]:
        return "JACKPOT!"
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return "WIN!"
    else:
        return "LOSE"
# スロットをプレイする関数
def play():
    print("Let\'s play the slot!")
    money = 100
    while money > 0:
        print("You have {} coins.".format(money))
        bet = int(input("How much do you bet? (1-10) "))
        if bet < 1 or bet > 10:
            print("Invalid bet amount.")
            continue
        reels = spin()
        display(reels)
        result = judge(reels)
        if result == "JACKPOT!":
            money += bet * 100
        elif result == "WIN!":
            money += bet * 10
        else:
            money -= bet
        print(result)
    print("Game over. You have no coins left.")
# スロットをプレイする
play()
