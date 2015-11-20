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

def PreOrder(node):
    if node:
        print(node.val)
        PreOrder(node.left)
        PreOrder(node.right)

def PostOrder(node):
    if node:
        PostOrder(node.left)
        PostOrder(node.right)
        print(node.val)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print('In-order tree traversal:')
InOrder(root)
print('Pre-order tree traversal:')
PreOrder(root)
print('Post-order tree traversal:')
PostOrder(root)

