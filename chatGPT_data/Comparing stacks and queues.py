class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
# スタックの使用例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("スタックの要素:")
while not stack.is_empty():
    print(stack.pop())
# キューの使用例
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("キューの要素:")
while not queue.is_empty():
    print(queue.dequeue())
