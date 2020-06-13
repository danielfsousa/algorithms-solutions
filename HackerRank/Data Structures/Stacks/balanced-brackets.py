# https://www.hackerrank.com/challenges/balanced-brackets/problem

from collections import deque

def isBalanced(s):
    if len(s) % 2 != 0:
        return 'NO'

    brackets_map = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    opening_brackets = brackets_map.keys()
    stack = deque()

    for char in s:
        if char in opening_brackets:
            stack.append(brackets_map[char])
        else:
            if len(stack) == 0:
                return 'NO'
            closing_bracket = stack.pop()
            if char != closing_bracket:
                return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'
