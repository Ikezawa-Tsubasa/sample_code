from copy import deepcopy

air = "."
bord = [[air for _ in range(8)] for _ in range(8)]
stone = {1:"○", 2:"●"}
bord[3][3] = "○"
bord[4][4] = "○"
bord[4][3] = "●"
bord[3][4] = "●"

# bord[3][3] = stone[2]
# bord[4][3] = stone[2]
# bord[5][3] = stone[2]


def view_bord(bord):
    print(" ", " ".join(map(str, range(8))))
    for i, bo in enumerate(bord):
        print(i, " ".join(bo))

def check_yoko(bord, yoko, tate, pl):
    bord_cp = bord.copy()
    me = stone[pl]
    you = 2 if pl == 1 else 1
    you = stone[you]
    # 置かれた石の左側を確認
    if me in bord[tate][:yoko]:
        ch_b = bord[tate][:yoko].copy()
        ch_b.reverse()
        ch_nows = ch_b[:ch_b.index(me)]
        # print(ch_b)
        # print(ch_nows)
        if air not in ch_nows and you in ch_nows:
            bord_cp[tate][len(ch_b)-1-ch_b.index(me):yoko] = [me]*(len(ch_nows)+1)
    # 置かれた石の右側を確認
    targ_ran = min(yoko+1, len(bord))
    if me in bord[tate][targ_ran:]:
        ch_b = bord[tate][targ_ran:].copy()
        ch_nows = ch_b[:min(ch_b.index(me), len(bord))]
        # print(ch_b)
        # print(ch_nows)
        if air not in ch_nows and you in ch_nows:
            bord_cp[tate][min(yoko+1, len(bord)):min(yoko+1+ch_b.index(me), len(bord))] = [me]*len(ch_nows)

    return bord_cp
            
def check_tate(bord, yoko, tate, pl):
    bord_cp = bord.copy()
    me = stone[pl]
    you = 2 if pl == 1 else 1
    you = stone[you]
    bord_cp = [list(x) for x in zip(*bord_cp)]
    # print(bord_cp[yoko][:tate])
    # 置かれた石の上側を確認
    if me in bord_cp[yoko][:tate]:
        ch_b = bord_cp[yoko][:tate].copy()
        ch_b.reverse()
        ch_nows = ch_b[:ch_b.index(me)]
        # print(ch_b)
        # print(ch_nows)
        
        if air not in ch_nows and you in ch_nows:
            # bord_cp[tate][len(ch_b)-1-ch_b.index(me):yoko] = [me]*(len(ch_nows)+1)
            bord_cp[yoko][len(ch_b)-1-ch_b.index(me):tate] = [me]*(len(ch_nows)+1)
    
    # 置かれた石の下側を確認
    targ_ran = min(tate+1, len(bord))
    if me in bord_cp[yoko][targ_ran:]:
        ch_b = bord_cp[yoko][targ_ran:].copy()
        ch_nows = ch_b[:ch_b.index(me)]
        # print(ch_b)
        # print(ch_nows)
        if air not in ch_nows and you in ch_nows:
            bord_cp[yoko][min(tate+1, len(bord)):min(tate+1+ch_b.index(me), len(bord))] = [me]*len(ch_nows)
    # if me in bord[yoko][min(tate)]

    bord_cp = [list(x) for x in zip(*bord_cp)]
    
    return bord_cp

def check_naname_right(bord, yoko, tate, pl):
    bord_cp = bord.copy()
    me = stone[pl]
    you = 2 if pl == 1 else 1
    you = stone[you]

    bord_cp = [list(x) for x in zip(*bord_cp)]
    n_y = yoko
    n_t = tate
    # 確認対象座標の取得
    ch_s = {(tate, yoko)}
    # print(ch_s, yoko, tate)
    for _ in range(len(bord_cp)):
        n_y += 1
        n_t += 1
        if n_y == yoko and n_t == tate:
            break
        if n_y == len(bord_cp):
            n_y -= n_t
            n_t = 0
        elif n_t == len(bord_cp[0]):
            n_t -= n_y
            n_y = 0
        ch_s.add((n_t, n_y))
    ch_s = list(ch_s)
    ch_s.sort()
    # print(ch_s)
    ch_b_alls = [bord_cp[ch_y][ch_t] for ch_t, ch_y in ch_s]
    # print(ch_b_alls)
    # 左上確認
    ch_b = ch_b_alls[:ch_s.index((tate, yoko))].copy()
    
    
    if me in ch_b:
        ch_b.reverse()
        ch_nows = ch_b[:ch_b.index(me)+1]
        if air not in ch_nows and you in ch_nows:
            ch_nows = [me]*(len(ch_nows)+1)
            ch_b_alls[ch_s.index((tate, yoko))-(len(ch_nows)-1):ch_s.index((tate, yoko))+1] = ch_nows
   
    
    ch_b = ch_b_alls[ch_s.index((tate, yoko))+1:].copy()
    # print(ch_s.index((tate, yoko))+1)
    # print(ch_b)
    if me in ch_b:
        ch_nows = ch_b[:ch_b.index(me)+1]
        # print(ch_nows)
        if air not in ch_nows and you in ch_nows:
            ch_nows = [me]*(len(ch_nows)+1)
            ch_b_alls[ch_s.index((tate, yoko)):ch_s.index((tate, yoko))+len(ch_nows)] = ch_nows
        
    # print(ch_b_alls)
    bord_cp = [list(x) for x in zip(*bord_cp)]
    for (ch_t, ch_y), st in zip(ch_s, ch_b_alls):
        bord_cp[ch_t][ch_y] = st
    return bord_cp
    
    
def check_naname_left(bord, yoko, tate, pl):
    bord_cp = bord.copy()
    me = stone[pl]
    you = 2 if pl == 1 else 1
    you = stone[you]

    bord_cp = [list(x) for x in zip(*bord_cp)]
    n_y = yoko
    n_t = tate
    # 確認対象座標の取得
    ch_s = {(tate, yoko)}
    # print(ch_s, yoko, tate)
    for _ in range(len(bord_cp)):
        n_y -= 1
        n_t += 1
        if n_y == yoko and n_t == tate:
            break
        if n_y == -1 or n_t == len(bord_cp[0]):
            tmp = n_y
            n_y = n_t-1
            n_t = tmp+1
        ch_s.add((n_t, n_y))
    ch_s = list(ch_s)
    ch_s.sort(key = lambda c:c[1])
    # print(ch_s)
    ch_b_alls = [bord_cp[ch_y][ch_t] for ch_t, ch_y in ch_s]
    # print(ch_b_alls)
    # 左下確認
    ch_b = ch_b_alls[:ch_s.index((tate, yoko))].copy()
    
    # print(ch_b_alls)
    if me in ch_b:
        ch_b.reverse()
        ch_nows = ch_b[:ch_b.index(me)+1]
        # print(ch_b, ch_nows)

        if air not in ch_nows and you in ch_nows:
            ch_nows = [me]*(len(ch_nows)+1)
            ch_b_alls[ch_s.index((tate, yoko))-(len(ch_nows)-1):ch_s.index((tate, yoko))+1] = ch_nows
   
    
    ch_b = ch_b_alls[ch_s.index((tate, yoko))+1:].copy()
    # print(ch_s.index((tate, yoko))+1)
    # print(ch_b)
    if me in ch_b:
        ch_nows = ch_b[:ch_b.index(me)+1]
        # print(ch_nows)
        if air not in ch_nows and you in ch_nows:
            ch_nows = [me]*(len(ch_nows)+1)
            ch_b_alls[ch_s.index((tate, yoko)):ch_s.index((tate, yoko))+len(ch_nows)] = ch_nows
    # print(ch_b_alls)
    bord_cp = [list(x) for x in zip(*bord_cp)]
    for (ch_t, ch_y), st in zip(ch_s, ch_b_alls):
        bord_cp[ch_t][ch_y] = st
    return bord_cp
    

def check_bord(bord, yoko, tate, pl):
    ch_algs = [check_tate, check_yoko, check_naname_right, check_naname_left]
    def _call_check(bord, alg_num=0):
        b = ch_algs[alg_num](bord, yoko, tate, pl)
        if alg_num == len(ch_algs)-1:
            return b
        return _call_check(b, alg_num+1)
    return _call_check(bord)


from pprint import pprint
def main():
    global bord
    pl = 2
    while True:
        
        view_bord(bord)
        pl = 2 if pl == 1 else 1
        print(f"プレイヤー{pl}({stone[pl]})の番です")

        tate, yoko = tuple(map(int, input("[縦 横]で入力してください：").split()))
        while not bord[tate][yoko] == air:
            print("その位置には既に石が置いてあります。")
            tate, yoko = tuple(map(int, input("[縦 横]で入力してください：").split()))
        bord[tate][yoko] = stone[pl]


        # bord = check_yoko(bord, yoko, tate, pl)
        # bord = check_tate(bord, yoko, tate, pl)
        # bord = check_naname_right(bord, yoko, tate, pl)
        # bord = check_naname_left(bord, yoko, tate, pl)

        bord = check_bord(bord, yoko, tate, pl)


if __name__ == "__main__":
    main()
    


    
    