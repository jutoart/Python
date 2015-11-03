#!/usr/local/bin/python3
# SortingAlgorithms.py
# Implement several kinds of sorting algorithms
# Author: Art.Huang

import sys

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


if len(sys.argv) < 2:
    print('Usage: SortingAlgorithms.py <input list of numbers>')
    exit()

print('Bubble Sort:')
print(BubbleSort([int(n) for n in sys.argv[1:]]))
print('Selection Sort:')
print(SelectionSort([int(n) for n in sys.argv[1:]]))
print('Insertion Sort:')
print(InsertionSort([int(n) for n in sys.argv[1:]]))
