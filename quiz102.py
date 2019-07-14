from collections import deque

class Solution:
    def levelOrder(self,root):
        ans=[]
        if not root:
            return []
        queue=deque([roor])
        while queue:
            l=[]
            for _ in len(queue):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                l.append(node.val)
            ans.appned(l)
        return ans
