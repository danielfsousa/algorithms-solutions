'''
Queue with two stacks. Implement a queue with two stacks so that each queue operations
makes a constant amortized number of stack operations.
'''


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


class QueueWithTwoStacks:
    def __init__(self):
        self.stack_newest_top = Stack()
        self.stack_oldest_top = Stack()

    def __shift_stacks(self):
        if self.stack_oldest_top.is_empty():
            while not self.stack_newest_top.is_empty():
                self.stack_oldest_top.push(self.stack_newest_top.pop())

    def enqueue(self, item):
        self.stack_newest_top.push(item)

    def dequeue(self):
        self.__shift_stacks()
        return self.stack_oldest_top.pop()

    def is_empty(self):
        return self.stack_newest_top.is_empty() and self.stack_oldest_top.is_empty()

    def size(self):
        return self.stack_newest_top.size() + self.stack_oldest_top.size()


queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.dequeue())
