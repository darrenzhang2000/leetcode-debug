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