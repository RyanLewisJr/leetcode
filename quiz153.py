class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index=0
        for i in range(len(nums)):
            if nums[i]<nums[min_index]:
                min_index=i
        return nums[min_index]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        start=0
        end=len(nums)-1
        if nums[0]<nums[end]:
            return nums[0]
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[0]:
                start=mid+1
            else:
                end=mid-1
