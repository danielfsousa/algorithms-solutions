'''
Stack with max.
Create a data structure that efficiently supports the stack operations (push and pop)
and also a return-the-maximum operation.
Assume the elements are real numbers so that you can compare them.
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

    def peek(self):
        if not self.is_empty():
            return self.first.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length


class StackWithMax:
    def __init__(self):
        self.numbers = Stack()
        self.max = Stack()

    def push(self, number):
        last_max = self.max.peek()
        new_max = max(last_max, number) if last_max is not None else number
        self.max.push(new_max)
        self.numbers.push(number)

    def pop(self):
        self.max.pop()
        return self.numbers.pop()

    def maximum(self):
        return self.max.peek()


stack = StackWithMax()
stack.push(10)
stack.push(32)
stack.push(3)
print(stack.pop())
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.pop())
print(stack.maximum())
