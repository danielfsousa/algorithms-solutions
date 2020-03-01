'''
Shuffling a linked list.
Given a singly-linked list containing n items, rearrange the items uniformly at random.
Your algorithm should consume a logarithmic (or constant) amount of extra memory and run
in time proportional n log n in the worst case.
'''
from random import randint


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

    def __len__(self):
        return self.length

    def __iter__(self):
        return QueueIterator(self)

    def __str__(self):
        values = [i for i in self]
        seperator = ', '
        return f'Queue({seperator.join(map(str, values))})'

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

    def get(self, index):
        for key, val in enumerate(self):
            if key == index:
                return val

    def is_empty(self):
        return self.length == 0


def shuffle(ll):
    def rand(ll, aux, low, high):
        if high <= low:
            return
        mid = (low + high) // 2
        rand(ll, aux, low, mid)
        rand(ll, aux, mid + 1, high)
        merge(ll, aux, low, mid, high)

    def merge(ll, aux, low, mid, high):
        low_node = ll.first
        for _ in range(low):
            low_node = low_node.next
        current_node = low_node

        # copy
        for n in range(low, high + 1):
            aux[n] = current_node.value
            current_node = current_node.next

        i = low
        j = mid + 1
        current_node = low_node
        for k in range(low, high + 1):
            if i > mid:
                current_node.value = aux[j]
                j += 1
            elif j > high:
                current_node.value = aux[i]
                i += 1
            elif randint(0, 1) > 0:
                current_node.value = aux[i]
                i += 1
            else:
                current_node.value = aux[j]
                j += 1
            current_node = current_node.next

    length = len(ll)
    rand(ll, aux=[None] * length, low=0, high=length - 1)


queue = Queue()
for i in range(1, 11):
    queue.enqueue(i)

print(queue)
shuffle(queue)
print(queue)
