class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#preorder
def preorderTraversal(node):
    if not node:
        return
    stack = []
    stack.append(node)
    while len(stack) > 0:
        x = stack.pop()
        print(x.val)
        if x.right:
            stack.append(x.right)
        if x.left:
            stack.append(x.left)
    return

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)
one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
preorderTraversal(one)

#inorder
def inorderTraversal(node):
    if not node:
        return
    stack = []
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            print(node)
            node = node.right

inorderTraversal(one)        


#postorder


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
            return []
        result = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        result.reverse()
        return result
        




one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
three.left = one
three.right = two

a = Solution()
# print(a.postorderTraversal(three))