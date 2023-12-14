import random
def omikuji():
    fortunes = ["大吉", "中吉", "小吉", "吉", "凶"]
    fortune = random.choice(fortunes)
    return fortune
result = omikuji()
print(result)
