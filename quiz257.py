class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result=[str(root.val)+'->'+path for path in self.binaryTreePaths(root.left)]
        result+=[str(root.val)+'->'+path for path in self.binaryTreePaths(root.right)]
        return result or [str(root.val)]
