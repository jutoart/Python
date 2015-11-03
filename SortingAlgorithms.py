#!/usr/local/bin/python3
# SortingAlgorithms.py
# Implement several kinds of sorting algorithms
# Author: Art.Huang

import sys
import random
from timeit import default_timer as timer

def MeasureTimeAndPrint(name, nums, func):
    t = timer()
    s = func(list(nums))
    print(name + ('%.4f' % (timer() - t)) + ' secs')
    print(s) if size <= visibleSize else None

def Ascending(x, y):
    return x - y

def Descending(x, y):
    return -Ascending(x, y)

def BubbleSort(nums, compare = Ascending):
    size = len(nums)

    for i in range(size):
        for j in range(size-1):
            if compare(nums[j], nums[j+1]) > 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        size -= 1

    return nums

def SelectionSort(nums, compare = Ascending):
    size = len(nums)

    for i in range(size-1):
        for j in range(i+1, size):
            if compare(nums[i], nums[j]) > 0:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

def InsertionSort(nums, compare = Ascending):
    size = len(nums)

    for i in range(1, size):
        j = i - 1

        while j >= 0:
            if compare(nums[j], nums[j+1]) > 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
            else:
                break

    return nums

def Quicksort(nums, compare = Ascending):
    stack = [(0, len(nums)-1)]

    while len(stack) > 0:
        (p, q) = stack.pop()

        if p < q:
            i = p
            j = i + 1

            while j <= q:
                if compare(nums[p], nums[j]) > 0:
                    nums[j], nums[i+1] = nums[i+1], nums[j]
                    i += 1

                j += 1
            
            nums[p], nums[i] = nums[i], nums[p]
            stack.append((p, i-1))
            stack.append((i+1, q))

    return nums

def RandomizedQuicksort(nums, compare = Ascending):
    stack = [(0, len(nums)-1)]

    while len(stack) > 0:
        (p, q) = stack.pop()

        if p < q:
            r = random.randint(p, q)
            nums[p], nums[r] = nums[r], nums[p]
            i = p
            j = i + 1

            while j <= q:
                if compare(nums[p], nums[j]) > 0:
                    nums[j], nums[i+1] = nums[i+1], nums[j]
                    i += 1

                j += 1
            
            nums[p], nums[i] = nums[i], nums[p]
            stack.append((p, i-1))
            stack.append((i+1, q))

    return nums


if len(sys.argv) != 2 or int(sys.argv[1]) < 0:
    print('Usage: SortingAlgorithms.py <test list size>')
    exit()

visibleSize = 30
size = int(sys.argv[1])

print('\n[Nearly Sorted]')
nums = list(range(size))

if size > 1:
    nums[int(size/2)-1], nums[int(size/2)] = nums[int(size/2)], nums[int(size/2)-1]

print(nums) if size <= visibleSize else None
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)
MeasureTimeAndPrint('Quicksort:  ', nums, Quicksort)
MeasureTimeAndPrint('Randomized Quicksort:  ', nums, RandomizedQuicksort)

print('\n[Reverse Sorted]')
nums = list(range(size, 0, -1))
print(nums) if size <= visibleSize else None
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)
MeasureTimeAndPrint('Quicksort:  ', nums, Quicksort)
MeasureTimeAndPrint('Randomized Quicksort:  ', nums, RandomizedQuicksort)

print('\n[Random Order]')
nums = list(range(size))
random.shuffle(nums)
print(nums) if size <= visibleSize else None
MeasureTimeAndPrint('Bubble Sort:  ', nums, BubbleSort)
MeasureTimeAndPrint('Selection Sort:  ', nums, SelectionSort)
MeasureTimeAndPrint('Insertion Sort:  ', nums, InsertionSort)
MeasureTimeAndPrint('Quicksort:  ', nums, Quicksort)
MeasureTimeAndPrint('Randomized Quicksort:  ', nums, RandomizedQuicksort)
