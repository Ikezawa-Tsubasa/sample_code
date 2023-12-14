import random
def janken():
    hands = ['グー', 'チョキ', 'パー']
    computer_hand = random.choice(hands)
    
    while True:
        player_hand = input('じゃんけんの手を入力してください（グー、チョキ、パー）: ')
        if player_hand in hands:
            break
        else:
            print('無効な手です。もう一度入力してください。')
    
    print('あなたの手:', player_hand)
    print('コンピュータの手:', computer_hand)
    
    if player_hand == computer_hand:
        print('引き分けです！')
    elif (player_hand == 'グー' and computer_hand == 'チョキ') or \
         (player_hand == 'チョキ' and computer_hand == 'パー') or \
         (player_hand == 'パー' and computer_hand == 'グー'):
        print('あなたの勝ちです！')
    else:
        print('あなたの負けです！')
janken()
