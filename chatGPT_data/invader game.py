game = StickGame(10)
game.print_sticks()  # Sticks left: 10
while not game.is_game_over():
    num = int(input("How many sticks do you want to take? "))
    if game.take_sticks(num):
        game.print_sticks()
print("Game over!")
