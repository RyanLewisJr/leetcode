class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        j=0
        k=len(nums)-1
        while j<=k:
            if nums[j] is 0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j] is 1:
                j+=1
            else:
                nums[j],nums[k]=nums[k],nums[j]
                k-=1
