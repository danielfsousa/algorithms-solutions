'''
Nuts and bolts.
A disorganized carpenter has a mixed pile of nnn nuts and nnn bolts.
The goal is to find the corresponding pairs of nuts and bolts.
Each nut fits exactly one bolt and each bolt fits exactly one nut.
By fitting a nut and a bolt together, the carpenter can see which one
is bigger(but the carpenter cannot compare two nuts or two bolts directly).
Design an algorithm for the problem that uses at most proportional to
n log n compares (probabilistically).
'''

from random import randint


def match_nuts_bolts(nuts, bolts):
    def shuffle(nuts, bolts):
        N = len(nuts)
        for i in range(N):
            r = randint(i, N)
            nuts[i], nuts[r] = nuts[r], nuts[i]
            bolts[i], bolts[r] = bolts[r], bolts[i]

    def partition(nuts, bolts, low, high):
        return nuts

    def sort(nuts, bolts, low, high):
        if high <= low:
            return
        p = partition(nuts, bolts, low, high)
        sort(nuts, bolts, low, p - 1)
        sort(nuts, bolts, p + 1, high)

        return nuts

    shuffle(nuts, bolts)
    sort(nuts, bolts, low=0, high=len(nuts) - 1)


nuts = ['e', 'a', 'b', 'd', 'c', 'f']
bolts = ['f', 'e', 'c', 'd', 'b', 'a']

print(nuts)   # a, b, c, d, e, f
print(bolts)  # a, b, c, d, e, f
