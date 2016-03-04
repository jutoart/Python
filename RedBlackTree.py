#!/usr/local/bin/python3
# RedBlackTree.py
# Implement Red-Black tree
# Author: Art.Huang

from enum import Enum
from random import randint

class Color(Enum):
    red = 0
    black = 1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.color = Color.red
        self.left = None
        self.right = None
        self.parent = None

    def Sibling(self):
        return None if not self.parent else self.parent.left if self.parent.right is self else self.parent.right

    def Uncle(self):
        return None if not self.parent or not self.parent.parent else self.parent.parent.left if self.parent.parent.right is self.parent else self.parent.parent.right

class RedBlackTree:
    def __init__(self):
        self.root = None

    def _Search(self, node, val):
        if not node:
            return None
        else:
            if node.val == val:
                return node
            elif node.val > val:
                return self._Search(node.left)
            else:
                return self._Search(node.right)

    def Search(self, val):
        self._Search(self.root, val)

    def _RotateLeft(self, parent, child):
        parent.right = child.left
        child.left = parent

        if parent.right:
            parent.right.parent = parent
        
        if parent.parent:
            if parent.parent.left is parent:
                parent.parent.left = child
            else:
                parent.parent.right = child

        child.parent = parent.parent
        parent.parent = child
        return
    
    def _RotateRight(self, parent, child):
        parent.left = child.right
        child.right = parent

        if parent.left:
            parent.left.parent = parent

        if parent.parent:
            if parent.parent.left is parent:
                parent.parent.left = child
            else:
                parent.parent.right = child

        child.parent = parent.parent
        parent.parent = child
        return child

    def _InsertSearch(self, node, val):
        if not node:
            return None
        else:
            if node.val >= val:
                if not node.left:
                    return node
                else:
                    return self._InsertSearch(node.left, val)
            else:
                if not node.right:
                    return node
                else:
                    return self._InsertSearch(node.right, val)

    def _CheckRedBlackForInsert(self, parent, child):
        if child.color == Color.red:
            if child is self.root:
                child.color = Color.black
            else:
                if parent.color == Color.red:
                    if parent is self.root:
                        parent.color = Color.black
                    else:
                        # Uncle's color is red
                        if child.Uncle() and child.Uncle().color == Color.red:
                            parent.color = Color.black
                            child.Uncle().color = Color.black
                            parent.parent.color = Color.red
                            self._CheckRedBlackForInsert(parent.parent.parent, parent.parent)
                        else:
                            # Uncle's color is black
                            if parent.parent.left is parent:
                                if child is parent.right:
                                    self._RotateLeft(parent, child)
                                    parent, child = child, parent

                                parent.parent.color = Color.red
                                parent.color = Color.black
                                self._RotateRight(parent.parent, parent)
                            else:
                                if child is parent.left:
                                    self._RotateRight(parent, child)
                                    parent, child = child, parent

                                parent.parent.color = Color.red
                                parent.color = Color.black
                                self._RotateLeft(parent.parent, parent)

    def Insert(self, val):
        parent = self._InsertSearch(self.root, val)

        if not parent:
            self.root = TreeNode(val)
            self.root.color = Color.black
        else:
            if parent.val >= val:
                parent.left = TreeNode(val)
                parent.left.parent = parent
                self._CheckRedBlackForInsert(parent, parent.left)
            else:
                parent.right = TreeNode(val)
                parent.right.parent = parent
                self._CheckRedBlackForInsert(parent, parent.right)

    def Delete(self, val):
        node = Search(val)

        if node:
            if not node.left and not node.right:
                if node.parent.left is node:
                    node.parent.left = None
                else:
                    node.parent.right = None

                if node.color == Color.black:
                    self._CheckRedBlackForDelete(node.parent.parent, node.parent)
            elif not node.left:
                if node.parent.left is node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                
                if node.color == Color.black:
                    self._CheckRedBlackForDelete(node.parent, node.right)
            elif not node.right:
                if node.parent.left is node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                
                if node.color == Color.black:
                    self._CheckRedBlackForDelete(node.parent, node.left)
            else:
                inOrderNext = node.right

                while inOrderNext.left:
                    inOrderNext = inOrderNext.left

                node.val = inOrderNext.val
                
                if inOrderNext.parent.left is inOrderNext:
                    inOrderNext.parent.left = inOrderNext.right
                else:
                    inOrderNext.parent.right = inOrderNext.right

                if inOrderNext.color == Color.black:
                    if inOrderNext.right:
                        self._CheckRedBlackForDelete(inOrderNext.parent, inOrderNext.right)
                    else:
                        self._CheckRedBlackForDelete(inOrderNext.parent.parent, inOrderNext.parent)

    def _Print(self, node):
        if node.left:
            self._Print(node.left)
        
        print(node.val, node.color)

        if node.right:
            self._Print(node.right)

        return

    def Print(self):
        self._Print(self.root)


insertVal = [randint(1, 100) for i in range(30)]
rbTree = RedBlackTree()

for val in insertVal:
    rbTree.Insert(val)

rbTree.Print()
