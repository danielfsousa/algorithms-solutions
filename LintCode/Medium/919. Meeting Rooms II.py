# https://www.lintcode.com/problem/meeting-rooms-ii/

from heapq import heappush, heappushpop


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals):
        """
        Time complexity: O(n log n)
        Space complexity: O(k)
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            current = intervals[i]
            earliest_end = heap[0]

            if current.start < earliest_end:
                heappush(heap, current.end)
            else:
                heappushpop(heap, current.end)

        return len(heap)
