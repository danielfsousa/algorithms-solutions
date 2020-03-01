class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueIterator():
    def __init__(self, queue):
        self.queue = queue
        self.index = queue.first

    def __next__(self):
        if self.index is None:
            raise StopIteration
        current = self.index.value
        self.index = self.index.next
        return current


class Queue:
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def __iter__(self):
        return QueueIterator(self)

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self.first = node
        else:
            self.last.next = node
        self.last = node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.first.value
        self.first = self.first.next
        self.length -= 1
        return item

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length


queue = Queue()
print(f'is empty: {queue.is_empty()}')

for x in range(10):
    queue.enqueue(x)

print(f'deque: {queue.dequeue()}')
print(f'size: {queue.size()}')

for item in queue:
    print(item)

print(f'is empty: {queue.is_empty()}')
print('dequeing...')

for item in queue:
    queue.dequeue()

print(f'is empty: {queue.is_empty()}')
print(f'size: {queue.size()}')
