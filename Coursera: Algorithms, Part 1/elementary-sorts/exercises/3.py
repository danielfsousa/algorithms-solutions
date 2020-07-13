'''
Dutch national flag.
Given an array of n buckets, each containing a red, white, or blue pebble,
sort them by color. The allowed operations are:

    swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
    color(i): determine the color of the pebble in bucket i.

The performance requirements are as follows:

    At most n calls to color().
    At most n calls to swap().
    Constant extra space.
'''

from enum import Enum
from random import shuffle


class Color(Enum):
    RED = 1
    WHITE = 2
    BLUE = 3


class DutchNationalFlag:
    def __init__(self, buckets):
        self.buckets = buckets

    def swap(self, i, j):
        self.buckets[i], self.buckets[j] = self.buckets[j], self.buckets[i]

    def color(self, i, c):
        self.buckets[i] = c

    def __partition(self, low, high):
        lt = low
        gt = high
        i = low
        pivot = self.buckets[low].value
        while i <= gt:
            if self.buckets[i].value < pivot:
                self.swap(lt, i)
                lt += 1
                i += 1
            elif self.buckets[i].value > pivot:
                self.swap(gt, i)
                gt -= 1
            else:
                i += 1
        return lt, gt

    def __3_way_quicksort(self, low, high):
        if low >= high:
            return
        lt, gt = self.__partition(low, high)
        self.__3_way_quicksort(low, lt - 1)
        self.__3_way_quicksort(gt + 1, high)

    def sort(self):
        low = 0
        high = len(self.buckets) - 1
        shuffle(self.buckets)
        self.__3_way_quicksort(low, high)


flag = DutchNationalFlag([Color.RED, Color.BLUE, Color.BLUE,
                          Color.RED, Color.WHITE, Color.BLUE,
                          Color.BLUE, Color.BLUE, Color.BLUE,
                          Color.WHITE, Color.WHITE, Color.RED])

flag.sort()
print(flag.buckets)  # RED, WHITE, BLUE
