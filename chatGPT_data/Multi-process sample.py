import multiprocessing
def worker(num):
    """ワーカープロセスの動作を定義する関数"""
    print(f'ワーカープロセス {num} を開始します')
    # ここにワーカープロセスの処理を記述する
    print(f'ワーカープロセス {num} を終了します')
if __name__ == '__main__':
    # プロセス数
    num_processes = 4
    # プロセスプールを作成
    pool = multiprocessing.Pool(processes=num_processes)
    # ワーカープロセスを実行
    for i in range(num_processes):
        pool.apply_async(worker, args=(i,))
    # プロセスプールを閉じて終了する
    pool.close()
    pool.join()
