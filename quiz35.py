class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        low,high=0,len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid] is target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return low
