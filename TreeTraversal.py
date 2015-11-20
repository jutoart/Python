#!/usr/local/bin/python3
# TreeTraversal.py
# Implement in-order, pre-order and post-order tree traversal
# Author: Art.Huang

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def InOrder(node):
    if node:
        InOrder(node.left)
        print(node.val)
        InOrder(node.right)

def InOrderStack(node):
    stack = []

    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) > 0:
                node = stack.pop()
                print(node.val)
                node = node.right
            else:
                break

def PreOrder(node):
    if node:
        print(node.val)
        PreOrder(node.left)
        PreOrder(node.right)

def PreOrderStack(node):
    stack = []
    stack.append(node) if node else None

    while len(stack) > 0:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

def PostOrder(node):
    if node:
        PostOrder(node.left)
        PostOrder(node.right)
        print(node.val)

def PostOrderStack(node):
    stack = []

    while True:
        if node:
            stack.append(node.right) if node.right else None
            stack.append(node)
            node = node.left
        else:
            if len(stack) > 0:
                node = stack.pop()

                if node.right and len(stack) > 0 and stack[-1] is node.right:
                    stack.pop()
                    stack.append(node)
                    node = node.right
                else:
                    print(node.val)
                    node = None

            else:
                break


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print('In-order tree traversal:')
InOrder(root)
print('Pre-order tree traversal:')
PreOrder(root)
print('Post-order tree traversal:')
PostOrder(root)
print('In-order tree traversal using stack:')
InOrderStack(root)
print('Pre-order tree traversal using stack:')
PreOrderStack(root)
print('Post-order tree traversal using stack:')
PostOrderStack(root)

