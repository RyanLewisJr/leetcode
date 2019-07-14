from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            l=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                l.append(node.val)
            ans.append(l)
        return list(reversed(ans))
