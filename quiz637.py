from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            s=0
            nodes=0
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                s+=node.val
                nodes+=1
            if nodes>0:
                ave=s/nodes
            ans.append(ave)
        return ans
