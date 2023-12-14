import threading
# スレッドで実行する関数
def print_numbers():
    for i in range(1, 6):
        print(i)
# メインスレッドで実行する処理
def main():
    # スレッドを作成して実行する
    thread = threading.Thread(target=print_numbers)
    thread.start()
    # メインスレッドの処理
    for i in range(6, 11):
        print(i)
    # スレッドの終了を待つ
    thread.join()
# メインスレッドで実行する
main()
