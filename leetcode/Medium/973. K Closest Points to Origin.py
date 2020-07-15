# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
from heapq import heappush, heappushpop


class Solution:
    def kClosest(self, points, K):
        """
        quick select recursive implementation

        Time complexity:  O(n) amortized / O(n^2) worst case
        Space complexity: O(n)
        """
        def partition(points, low, high):
            pivot = points[high]
            a = low
            for i in range(low, high):
                if self.distance(points[i]) <= self.distance(pivot):
                    points[a], points[i] = points[i], points[a]
                    a += 1
            points[a], points[high] = points[high], points[a]
            return a

        def sort(points, low, high, K):
            if low < high:
                p = partition(points, low, high)
                if p == K:
                    return
                elif p < K:
                    sort(points, p + 1, high, K)
                else:
                    sort(points, low, p - 1, K)

        sort(points, 0, len(points) - 1, K)
        return points[:K]

    def kClosestQuickSelect(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        quick select iterative implementation

        Time complexity:  O(n) amortized / O(n ^ 2) worst case
        Space complexity: O(1)
        """
        def partition(points, low, high):
            i = low
            j = high
            pivot = low
            while True:
                # find item on left to swap
                while self.distance(points[i]) <= self.distance(points[pivot]):
                    i += 1
                    if i == high:
                        break

                # find item on right to swap:
                while self.distance(points[pivot]) <= self.distance(points[j]):
                    j -= 1
                    if j == pivot:
                        break

                # break if pointers cross
                if i >= j:
                    break

                # swap
                points[i], points[j] = points[j], points[i]

            # swap with partitioning item
            points[pivot], points[j] = points[j], points[pivot]
            return j

        low = 0
        high = len(points) - 1

        while low < high:
            p = partition(points, low, high)
            if p < K:
                low = p + 1
            elif p > K:
                high = p - 1
            else:
                break
        return points[:K]

    def kClosestHeap(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        heap approach

        Time complexity:  O(n log k)
        Space complexity: O(k)
        """
        maxheap = []

        for point in points:
            distance = self.distance(point)
            if len(maxheap) == K:
                heappushpop(maxheap, (-distance, point))
            else:
                heappush(maxheap, (-distance, point))

        return [x[1] for x in maxheap]

    def distance(self, point):
        x, y = point
        return x ** 2 + y ** 2
