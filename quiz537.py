from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        count=Counter(nums)
        pairs=set([])
        
        for num in count:
            if k==0:
                if count[num]>1:
                    pairs.add((num,num))
            else:
                otherNum=num+k
                if otherNum in count:
                    pairs.add((num,otherNum) if num<=otherNum else pairs.add(otherNum,num))
        return len(pairs)
