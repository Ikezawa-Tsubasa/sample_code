class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False
# ハッシュテーブルの作成
hash_table = HashTable(10)
# データの追加
hash_table.insert(5, "apple")
hash_table.insert(2, "banana")
hash_table.insert(15, "cherry")
# デ'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。'}][{'role': 'system', 'content': 'プログラム部分はPythonで記述してください。実行例は表示しないでください。
