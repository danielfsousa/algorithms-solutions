# https://leetcode.com/problems/reorder-data-in-log-files/

import heapq
from typing import List


class Solution:
    """
    Keeps a list to numbers logs and a heap to sort words logs based on id, then concatenate them.

    Time complexity:  O(n log n)
    Space complexity: O(n)
    """

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        result = []

        for log in logs:
            log_id, rest = log.split(' ', 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                heapq.heappush(letter_logs, (rest, log_id))

        while letter_logs:
            rest, log_id = heapq.heappop(letter_logs)
            result.append(log_id + ' ' + rest)

        return result + digit_logs
