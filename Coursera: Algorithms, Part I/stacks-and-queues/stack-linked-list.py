class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackIterator():
    def __init__(self, stack):
        self.stack = stack
        self.index = stack.first

    def __next__(self):
        if self.index is None:
            raise StopIteration
        current = self.index.value
        self.index = self.index.next
        return current


class Stack:
    def __init__(self):
        self.length = 0
        self.first = None

    def __iter__(self):
        return StackIterator(self)

    def push(self, item):
        node = Node(item)
        if not self.is_empty():
            node.next = self.first
        self.first = node
        self.length += 1

    def pop(self):
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


stack = Stack()
print(f'is empty: {stack.is_empty()}')

for x in range(10):
    stack.push(x)

print(f'pop: {stack.pop()}')
print(f'size: {stack.size()}')

for item in stack:
    print(item)

print(f'is empty: {stack.is_empty()}')
print('popping...')

for item in stack:
    stack.pop()

print(f'is empty: {stack.is_empty()}')
print(f'size: {stack.size()}')
