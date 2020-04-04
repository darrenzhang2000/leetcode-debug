#preorder

#inorder

#postorder
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         self.helper(root, result)
#         return result
        
        
#     def helper(self, node, result):
#         if not node:
#             return
#         self.helper(node.left, result)
#         self.helper(node.right, result)
#         result.append(node.val)

    def postorderTraversal(self, root):
        if not root: 
            return 
        result = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack[-1]
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            x = stack.pop().val
            print(x, stack)
            result.append(x)
        return result
    
class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




one = treeNode(1)
two = treeNode(2)
three = treeNode(3)
one.right = two
two.left = three

a = Solution()
a.postorderTraversal(one)