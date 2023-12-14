# randomモジュールからchoiceをインストール
from random import choice
# tkinterモジュールのインストール
import tkinter

# Wodleクラスの実装
class Wordle():
    # イニシャライザを設定
    def __init__(self) -> None:
        # インスタンス変数の設定
        # word_hints:ヒントリスト 
        # word_unuse: 使わない文字のセット
        # count:挑戦回数
        self.word_hints = list()
        self.word_unuse = set()
        self.count = 0
        # ワードリストの読み込み
        with open(file="Swimmy/wordle/word5char_list.txt", mode="r") as f:
            words = [a.strip().split("\t") for a in f.readlines()]
        self.words = [w.lower() for word in words for w in word]
        # 答えの設定
        self.ans = choice(self.words)
        # ボードの左上座標の変数を125, 100のタプルで保存
        self.bord_left_up = 125, 100

    # startメソッドの実装
    def start(self) -> None:
        '''
        呼び出されたらゲームを開始
        '''
        # 全体実行
        # ウィンドウの生成
        self.root = tkinter.Tk()
        # ウィンドウタイトルをWordleに設定
        self.root.title("Wordle")
        # ウィンドウサイズを500x600に設定
        self.root.geometry('500x600')
        # キャンバスの作成。背景色を#f0f8ffに設定
        self.canvas = tkinter.Canvas(self.root, width=500, height=600, bg="#f0f8ff")
        # キャンバスの配置
        self.canvas.pack()
        # マスの表示
        # 5回繰り返す
        for i in range(5):
            # 5回繰り返す  
            for j in range(5):
                # 矩形の描画。色は白。
                self.canvas.create_rectangle(self.bord_left_up[0] +i*50, self.bord_left_up[1]+j*50,
                                        self.bord_left_up[0]+(i+1)*50, self.bord_left_up[1]+(j+1)*50, fill="white")
        # unused_strsの文字を表示。座標は250, 400,フォントは"HG丸ｺﾞｼｯｸM-PRO", フォントサイズは24
        self.canvas.create_text(250, 400, text="unused_strs", font=("HG丸ｺﾞｼｯｸM-PRO",24))
        # エラー表示用の矩形を描画。色は#f8f8ff
        self.canvas.create_rectangle(50, 360, 450, 385, fill="#f8f8ff", width=0)
        # 使わない文字一覧の為の矩形を描画。色は#dcdcdc
        self.canvas.create_rectangle(50, 425, 450, 600, fill="#dcdcdc", width=0)

        # 文字入力のエントリを生成
        self.entry = tkinter.Entry(self.root, width=25)
        # エントリの配置。175, 50
        self.entry.place(x=175, y=50)
        # ボタンの生成
        button = tkinter.Button(self.root, width=5, text="guess")
        # ボタンの配置。350, 47.5
        button.place(x=350, y=47.5)
        # ボタンにcheck関数を紐づけ。動作は左クリック。
        button.bind("<1>", self.check)
        # 残りチャレンジ可能回数を表示するラベルの生成
        self.label = tkinter.Label(self.root, text=f"残り:{5-self.count}回")
        # ラベルの配置。10, 10
        self.label.place(x=10, y=10)
        # ウィンドウを表示
        self.root.mainloop()
            

    # guessメソッドの実装。引数はword。
    def guess(self, word) -> list:
        '''
        文字を受け取って正解かどうかの判定を行う
        '''
        # エラー表示用の矩形を描画。色は#f8f8ff
        self.canvas.create_rectangle(50, 360, 450, 385, fill="#f8f8ff", width=0)
        # ヒントリストの初期化
        self.word_hints = list()
        # もし 入力文字数が5文字でない　なら
        if len(word) != 5:
            # 文字列 not enough letters を表示。座標は250, 370
            self.canvas.create_text(250, 370, text="not enough letters", font=("HG丸ｺﾞｼｯｸM-PRO",12))
            # 関数から抜け出す(戻り値なしでreturn)
            return
        # もし 入力文字が文字列のリストに入っていない　なら
        if word not in self.words:
            # 文字列 not in word list を表示。座標は250, 370
            self.canvas.create_text(250, 370, text="not in word list", font=("HG丸ｺﾞｼｯｸM-PRO",12))
            # 関数から抜け出す(戻り値なしでreturn)
            return 
        # 5回繰り返す
        for i in range(5):
            # もし 繰り返し番目の文字　が　答えの繰り返し番目の文字と同じ　なら
            if word[i] == self.ans[i]:
                # ヒントリストにgreenを追加
                self.word_hints.append("green")
            # でなければもし　繰り返し番目の文字が　答えの文字列に含まれている　なら
            elif word[i] in self.ans:
                # ヒントリストにyellowを追加
                self.word_hints.append("yellow")
            # でなければ
            else:
                # ヒントリストにgreenを追加
                self.word_hints.append("white")
                # 使わない文字のセットに文字を追加
                self.word_unuse.add(word[i])
        # 挑戦回数を1増やす
        self.count += 1
        # 残りチャレンジ可能回数を表示するラベルの生成と配置
        self.label = tkinter.Label(self.root, text=f"残り:{5-self.count}回")
        self.label.place(x=10, y=10)
        # ヒントリストを返す
        return self.word_hints
    
    # unusedメソッド -> 削除

    # game_finishメソッドの作成。引数として文字列sを受け取る(インスタンスメソッドである点に留意)
    # ゲームが終了したときに実行するメソッド
    def game_finish(self, s):
        # 500x600の大きさの矩形を0, 0に描画。色は#f0f8ff
        self.canvas.create_rectangle(0, 0, 500, 600, fill="#f0f8ff", width=0)
        # 受け取ったテキストを表示。座標は250, 300
        self.canvas.create_text(250, 300, text=s, font=("HG丸ｺﾞｼｯｸM-PRO",48))
        # 答えの表示。座標は250, 350
        self.canvas.create_text(250, 350, text=f"答え：{self.ans}", font=("HG丸ｺﾞｼｯｸM-PRO",24))

    
    # checkメソッドの作成。引数としてイベント(引数名はeとする)を受け取る(インスタンスメソッドである点に留意)
    # 入力文字を確認するメソッド。
    def check(self, e):
        # エントリ内の文字を取得
        inpt = self.entry.get()
        # エントリ内の文字を削除
        self.entry.delete(0, tkinter.END)
        # もし　入力がunuse なら
        if inpt == "unuse":
            # 関数から抜け出す(戻り値なしでreturn)
            return
        # guessメソッドを呼び出す。戻り値を変数で取得
        ret = self.guess(inpt)
        # もし　戻り値がNone　なら
        if ret == None:
            # 関数から抜け出す(戻り値なしでreturn)
            return
        # でなければもし　クリアしている　なら
        elif len(set(ret)) == 1 and "green" in ret:
            # game_finishメソッドを実行。引数にCLEARを渡す。
            self.game_finish("CLEAR")
        # でなければもし　countが5　なら
        elif self.count == 5:
            # game_finishメソッドを実行。引数にGAMEOVERを渡す。
            self.game_finish("GAMEOVER")
        # でなければ
        else:
            # 入力文字数回繰り返す
            for i in range(len(inpt)):
                # 矩形を描画。横方向は繰り返し回数, 縦方向はcountを下に座標を計算。1マス50x50で作成
                # 初期座標はボードの左上座標
                # 色は戻り値の繰り返し回数番目を使用
                self.canvas.create_rectangle(self.bord_left_up[0]+i*50, self.bord_left_up[1]+(self.count-1)*50, 
                                        self.bord_left_up[0]+(i+1)*50, self.bord_left_up[1]+self.count*50, fill=ret[i])
                # テキストを描画。入力文字の繰り返し番目を使用
                # 初期座標はボードの左上座標に経ても横も22.5を足したもの
                self.canvas.create_text(self.bord_left_up[0]+22.5+i*50, self.bord_left_up[1]+22.5+(self.count-1)*50, text=inpt[i], font=("HG丸ｺﾞｼｯｸM-PRO",24))

            '''
            for i, (s, color) in enumerate(zip(inpt, ret)):
                self.canvas.create_rectangle(self.bord_left_up[0]+i*50, self.bord_left_up[1]+(self.count-1)*50, 
                                        self.bord_left_up[0]+(i+1)*50, self.bord_left_up[1]+self.count*50, fill=color)
                self.canvas.create_text(self.bord_left_up[0]+22.5+i*50, self.bord_left_up[1]+22.5+(self.count-1)*50, text=s, font=("HG丸ｺﾞｼｯｸM-PRO",24))
            '''
            # 使わない文字一覧の為の矩形を描画。色は#dcdcdc
            self.canvas.create_rectangle(50, 425, 450, 800, fill="#dcdcdc", width=0)
            # 使わない文字のセットをソートして変数に保存
            sorted_unuse = sorted(self.word_unuse)
            # ソートした後の配列の長さ回繰り返す
            for i in range(len(sorted_unuse)):
                # 使わない文字を表示。横座標は繰り返し回数をもとに計算。15ずつずらす
                # 初期座標は100, 450
                # 表示文字はソートした後の配列の繰り返し回数番目
                self.canvas.create_text(100+i*15, 450, text=sorted_unuse[i], font=("HG丸ｺﾞｼｯｸM-PRO",12))
            '''
            for i, s in enumerate(sorted(self.word_unuse)):
                self.canvas.create_text(100+i*15, 450, text=s, font=("HG丸ｺﾞｼｯｸM-PRO",12))
            '''
                
    

# Wordleクラスのインスタンスを作成
w = Wordle()
# startメソッドを呼び出し
w.start()