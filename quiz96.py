class Solution:
    def numTrees(self, n: int) -> int:
        def factory(k):
            if k<=1:
                return 1
            else:
                return k*factory(k-1)
        if n<=1:
            return 1
        else:
            return int(factory(2*n)/(factory(n+1)*factory(n)))
