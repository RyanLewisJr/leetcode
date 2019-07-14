class Solution:
    min_val,prev=float('inf'),float('inf')
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(tree):
            if tree:
                inorder(tree.left)
                self.min_val=min(self.min_val,abs(self.prev-tree.val))
                self.prev=tree.val
                inorder(tree.right)
        inorder(root)
        return self.min_val
