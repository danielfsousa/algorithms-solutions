# https://www.lintcode.com/problem/meeting-rooms

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals):
        """
        Time complexity:  O(n log n)
        Space complexity: O(1)
        """
        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)
        earliest_end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start < earliest_end:
                return False
            else:
                earliest_end = interval.end

        return True
