#!/usr/local/bin/python3
# MinHeap.py
# Implement a min heap structure with no duplicated numbers
# Author: Art.Huang

class MinHeap():
    def __init__(self):
        self.heapArray = []
        self.length = 0

    def Insert(self, n):
        self.heapArray.append(n)
        self.length += 1
        i = self.length

        while i > 1 and self.heapArray[i-1] < self.heapArray[int(i/2)-1]:
                self.heapArray[i-1], self.heapArray[int(i/2)-1] = self.heapArray[int(i/2)-1], self.heapArray[i-1]
                i = i / 2

        while i <= self.length / 2:
            if i*2 == self.length or self.heapArray[i*2-1] <= self.heapArray[i*2]:
                if self.heapArray[i-1] > self.heapArray[i*2-1]:
                    self.heapArray[i-1], self.heapArray[i*2-1] = self.heapArray[i*2-1], self.heapArray[i-1]
                    i = i * 2
                else:
                    break
            else:
                if self.heapArray[i-1] > self.heapArray[i*2]:
                    self.heapArray[i-1], self.heapArray[i*2] = self.heapArray[i*2], self.heapArray[i-1]
                    i = i * 2 + 1
                else:
                    break

    def Delete(self, n):
        if self.length == 0:
            return

        i = 0

        for i in range(self.length):
            if self.heapArray[i] == n:
                break

        if self.heapArray[i] != n:
            return
        else:
            self.heapArray[i], self.heapArray[self.length-1] = self.heapArray[self.length-1], self.heapArray[i]
            self.heapArray.pop()
            self.length -= 1
            i += 1

        while i <= self.length / 2:
            if i*2 == self.length or self.heapArray[i*2-1] <= self.heapArray[i*2]:
                if self.heapArray[i-1] > self.heapArray[i*2-1]:
                    self.heapArray[i-1], self.heapArray[i*2-1] = self.heapArray[i*2-1], self.heapArray[i-1]
                    i = i * 2
                else:
                    break
            else:
                if self.heapArray[i-1] > self.heapArray[i*2]:
                    self.heapArray[i-1], self.heapArray[i*2] = self.heapArray[i*2], self.heapArray[i-1]
                    i = i * 2 + 1
                else:
                    break

    def GetMin(self):
        return None if self.length == 0 else self.heapArray[0]

    def Print(self):
        print(self.heapArray)

