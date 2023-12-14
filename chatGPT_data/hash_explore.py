class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    def _hash_function(self, key):
        return key % self.size
    def insert(self, key, value):
        hash_value = self._hash_function(key)
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i] = (key, value)
                return
        self.table[hash_value].append((key, value))
    def search(self, key):
        hash_value = self._hash_function(key)
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]
        return None
