# https://www.hackerrank.com/challenges/find-the-running-median/problem

import os
import sys
from heapq import heapify, heappush, heappop


class MedianHeap:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def add(self, num):
        if not self.maxheap and not self.minheap:
            heappush(self.maxheap, -num)
        else:
            if num >= -self.maxheap[0]:
                heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num)
        self.rebalance()

    def median(self):
        if len(self.maxheap) == len(self.minheap):
            first_mid = -self.maxheap[0]
            second_mid = self.minheap[0]
            return (first_mid + second_mid) / 2
        elif len(self.maxheap) == len(self.minheap) + 1:
            return float(-self.maxheap[0])
        elif len(self.minheap) == len(self.maxheap) + 1:
            return float(self.minheap[0])
        else:
            self.rebalance()
            return self.median()

    def rebalance(self):
        if len(self.minheap) == len(self.maxheap) + 2:
            min_num = heappop(self.minheap)
            heappush(self.maxheap, -min_num)
        elif len(self.maxheap) == len(self.minheap) + 2:
            max_num = heappop(self.maxheap)
            heappush(self.minheap, -max_num)


#
# Complete the runningMedian function below.
#
def runningMedian(a):
    heaps = MedianHeap()
    medians = []
    for num in a:
        heaps.add(num)
        medians.append(heaps.median())
    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
