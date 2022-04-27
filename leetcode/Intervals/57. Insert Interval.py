from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Sliding window like. Keep merging the overlapping intervals

        Time complexity:  O(n)
        Space complexity: O(n)
        """

        def is_before(a, b):
            return a[1] < b[0]

        def is_after(a, b):
            return a[0] > b[1]

        def merge_overlapping(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        res = []

        for i in range(len(intervals)):
            if is_before(newInterval, intervals[i]):
                res.append(newInterval)
                return res + intervals[i:]
            elif is_after(newInterval, intervals[i]):
                res.append(intervals[i])
            else:
                newInterval = merge_overlapping(intervals[i], newInterval)

        res.append(newInterval)

        return res
