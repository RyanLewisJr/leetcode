class Solution:
    def pathSum(self, root: TreeNode, total: int) -> int:
        if not root:
            return 0
        num=0
        stack=[(root,[root.val])]
        while stack:
            node,totals=stack.pop()
            num+=totals.count(total)
            if node.left:
                stack.append((node.left,[x+node.left.val for x in totals]\
                              +[node.left.val]))
            if node.right:
                stack.append((node.right,[x+node.right.val for x in totals]\
                              +[node.right.val]))
        return num

class Solution1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                res.append("{}{}".format(path,node.val))
            stack.append((node.left, "{}{}->".format(path,node.val)))
            stack.append((node.right, "{}{}->".format(path,node.val)))
        return res
