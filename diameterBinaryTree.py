'''
Lesson: if you ever need a variable which you want to modify, just create it in the local scope and define a 
function within that scope which modifies the local variable. 

Python higher ordered functions!!
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_ = 1
        def helper(node):
            if not node: 
                return 0
            L = helper(node.left)
            R = helper(node.right)
            self.max_ = max(self.max_, 1 + L + R)
            return 1 + max(L, R)
        helper(root)
        return self.max_ - 1