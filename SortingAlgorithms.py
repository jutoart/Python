#!/usr/local/bin/python3
# SortingAlgorithms.py
# Implement several kinds of sorting algorithms
# Author: Art.Huang

import sys
import random
from timeit import default_timer as timer

def MeasureTimeAndPrint(name, nums, func):
    t = timer()
    s = func(nums)
    print(name + ('%.4f' % (timer() - t)) + ' secs')
    print(s) if size <= visibleSize else None

def Ascending(x, y):
    return x - y

def Descending(x, y):
    return -Ascending(x, y)

def _BubbleUp(nums, compare):
    return nums if len(nums) <= 1 else [nums[1]] + _BubbleUp([nums[0]] + nums[2:], compare) if compare(nums[0], nums[1]) > 0 else [nums[0]] + _BubbleUp(nums[1:], compare)

def BubbleSort(nums, compare = Ascending):
    nums = _BubbleUp(nums, compare)
    return nums if len(nums) <= 1 else BubbleSort(nums[:-1], compare) + [nums[-1]]

def SelectionSort(nums, compare = Ascending):
    sel = 0

    for i in range(1, len(nums)):
        if compare(nums[i], nums[sel]) > 0:
            sel = i

    return nums if len(nums) <= 1 else SelectionSort(nums[:sel] + nums[sel+1:], compare) + [nums[sel]]

def _Insert(nums, compare):
    sortedNums = InsertionSort(nums[1:], compare)
    return [n for n in sortedNums if compare(nums[0], n) >= 0] + [nums[0]] + [n for n in sortedNums if compare(nums[0], n) < 0]

def InsertionSort(nums, compare = Ascending):
    return nums if len(nums) <= 1 else _Insert(nums, compare)


if len(sys.argv) != 2:
    print('Usage: SortingAlgorithms.py <test list size>')
    exit()

visibleSize = 30
size = int(sys.argv[1])

print('\n[Nearly Sorted]')
nums = list(range(size))

if size > 1:
    nums[int(size/2)-1], nums[int(size/2)] = nums[int(size/2)], nums[int(size/2)-1]

print('' + str(nums)) if size <= visibleSize else None
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)

print('\n[Reverse Sorted]')
nums = list(range(size, 0, -1))
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)

print('\n[Random Order]')
nums = list(range(size))
random.shuffle(nums)
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)
