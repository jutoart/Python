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
                return self._Search(node.left, val)
            else:
                return self._Search(node.right, val)

    def Search(self, val):
        return self._Search(self.root, val)

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

        if self.root is parent:
            self.root = child

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

        if self.root is parent:
            self.root = child

        return

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

    def _CheckRedBlackForInsert(self, node):
        if node.color == Color.red:
            if node is self.root:
                node.color = Color.black
            else:
                if node.parent.color == Color.red:
                    if node.parent is self.root:
                        node.parent.color = Color.black
                    else:
                        # Uncle's color is red
                        if node.Uncle() and node.Uncle().color == Color.red:
                            node.parent.color = Color.black
                            node.Uncle().color = Color.black
                            node.parent.parent.color = Color.red
                            self._CheckRedBlackForInsert(node.parent.parent)
                        else:
                            # Uncle's color is black
                            if node.parent.parent.left is node.parent:
                                if node is node.parent.right:
                                    self._RotateLeft(node.parent, node)
                                else:
                                    node = node.parent
                                node.parent.color = Color.red
                                node.color = Color.black
                                self._RotateRight(node.parent, node)
                            else:
                                if node is node.parent.left:
                                    self._RotateRight(node.parent, node)
                                else:
                                    node = node.parent
                                node.parent.color = Color.red
                                node.color = Color.black
                                self._RotateLeft(node.parent, node)

    def Insert(self, val):
        parent = self._InsertSearch(self.root, val)

        if not parent:
            self.root = TreeNode(val)
            self.root.color = Color.black
        else:
            if parent.val >= val:
                parent.left = TreeNode(val)
                parent.left.parent = parent
                self._CheckRedBlackForInsert(parent.left)
            else:
                parent.right = TreeNode(val)
                parent.right.parent = parent
                self._CheckRedBlackForInsert(parent.right)

    def _CheckRedBlackForDelete(self, node):
        if node is self.root or node.color == Color.red:
            node.color = Color.black
        else:
            # Case 1: Sibling's color is red
            if node.Sibling().color == Color.red:
                node.parent.color = Color.red
                node.Sibling().color = Color.black

                if node is node.parent.left:
                    self._RotateLeft(node.parent, node.Sibling())
                else:
                    self._RotateRight(node.parent, node.Sibling())

                self._CheckRedBlackForDelete(node)
            else:
                siblingLeftColor = Color.black if not node.Sibling().left else node.Sibling().left.color
                siblingRightColor = Color.black if not node.Sibling().right else node.Sibling().right.color

                # Case 2: Sibling's color is black and all its children's color are black
                if siblingLeftColor == Color.black and siblingRightColor == Color.black:
                    node.Sibling().color = Color.red
                    self._CheckRedBlackForDelete(node.parent)
                # Case 3: Sibling's color is black and its same-direction child's color is red
                elif node is node.parent.left and siblingLeftColor == Color.red:
                    node.Sibling().color = Color.red
                    node.Sibling().left.color = Color.black
                    self._RotateRight(node.Sibling(), node.Sibling().left)
                    self._CheckRedBlackForDelete(node)
                elif node is node.parent.right and siblingRightColor == Color.red:
                    node.Sibling().color = Color.red
                    node.Sibling().right.color = Color.black
                    self._RotateLeft(node.Sibling(), node.Sibling().right)
                    self._CheckRedBlackForDelete(node)
                # Case 4: Sibling's color is black and its other-direction child's color is red
                else:
                    node.Sibling().color = node.parent.color
                    node.parent.color = Color.black

                    if node is node.parent.left:
                        node.Sibling().right.color = Color.black
                        self._RotateLeft(node.parent, node.Sibling())
                    else:
                        node.Sibling().left.color = Color.black
                        self._RotateRight(node.parent, node.Sibling())

    def Delete(self, val):
        node = self.Search(val)

        if node:
            if not node.left and not node.right:
                self._CheckRedBlackForDelete(node)

                if node.parent.left is node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            elif not node.left:
                if node.parent.left is node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                if node.color == Color.red:
                    node.right.color = Color.red

                node.right.parent = node.parent
                self._CheckRedBlackForDelete(node.right)
            elif not node.right:
                if node.parent.left is node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                if node.color == Color.red:
                    node.left.color = Color.red

                node.left.parent = node.parent
                self._CheckRedBlackForDelete(node.left)
            else:
                inOrderNext = node.right

                while inOrderNext.left:
                    inOrderNext = inOrderNext.left

                node.val = inOrderNext.val
                
                if inOrderNext.right:
                    if inOrderNext.parent.left is inOrderNext:
                        inOrderNext.parent.left = inOrderNext.right
                    else:
                        inOrderNext.parent.right = inOrderNext.right

                    self._CheckRedBlackForDelete(inOrderNext.right)
                else:
                    self._CheckRedBlackForDelete(inOrderNext)

                    if inOrderNext.parent.left is inOrderNext:
                        inOrderNext.parent.left = None
                    else:
                        inOrderNext.parent.right = None

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
print()

for i in range(10):
    index = randint(0, len(insertVal)-1)
    print("Delete: " + str(insertVal[index]))
    rbTree.Delete(insertVal[index])
    insertVal = insertVal[:index] + insertVal[index+1:]

print()
rbTree.Print()
