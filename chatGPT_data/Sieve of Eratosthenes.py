def eratosthenes(n):
    # 2からnまでの数列を作成
    numbers = list(range(2, n+1))
    primes = []
    while numbers:
        # 数列の先頭の数を素数リストに追加
        prime = numbers.pop(0)
        primes.append(prime)
        # 数列からprimeの倍数を削除
        for i in range(prime*2, n+1, prime):
            if i in numbers:
                numbers.remove(i)
    return primes
