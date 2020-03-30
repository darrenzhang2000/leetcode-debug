class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.ht = {}
        for ind, val in enumerate(inorder):
            self.ht[val] = ind
        return self.helper(preorder, inorder)


    def helper(self, preorder, inorder):
        if len(inorder) == 0:
            return
        if not preorder:
            return
        root_v = preorder[0]
        index = self.ht[preorder[0]]
        root = TreeNode(inorder[self.ht[preorder[0]]])
        
        #The problem is that the by using the hashtable, we must pass the original inorder array
        #instead, i incorrectly passed the sliced array.
        root.left = self.helper(preorder[1: index + 1], inorder[:index])
        root.right = self.helper(preorder[index+1:], inorder[index+1:])
        return root

a = Solution()
a.buildTree([3,9,20,15,7], [9,3,15,20,7])