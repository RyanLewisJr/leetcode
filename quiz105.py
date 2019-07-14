class Solution(object):
    def helper(self,l1,h1,l2,h2,preorder,inorder):
        if l1>len(preorder)-1 or l2>h2:
            return None
        root=TreeNode(preorder[l1])
        i=l2
        while inorder[i]!=root.val:
            i+=1
        llen=i-l2
        rlen=h2-i
        if llen:
            root.left=self.helper(l1+1,l1+llen,l2,l2+llen-1,preorder,inorder)
        else:
            root.left=None
        if rlen:
            root.right=self.helper(h1-rlen+1,h1,h2-rlen+1,h2,preorder,inorder)
        else:
            root.right=None
        return root

    def buildTree(self, preorder, inorder):
        return self.helper(0,len(preorder)-1,0,len(inorder)-1,preorder,inorder)
        
