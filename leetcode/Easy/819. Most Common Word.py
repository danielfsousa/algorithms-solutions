# https://leetcode.com/problems/most-common-word/

import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Time complexity:  O(n)
        Space compelxity: O(n)
        """
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        counter = Counter(w for w in words if w not in banned)
        return counter.most_common(1)[0][0]
