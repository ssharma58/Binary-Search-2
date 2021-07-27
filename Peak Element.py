class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if(len(nums)==0 and nums==None):
            return -1
        while(low<=high):
            mid=low+(high-low)/2
            mid=int(mid)
           
            if(((mid==len(nums)-1 or nums[mid+1]<nums[mid])) and (mid==0 or (nums[mid-1]<nums[mid]))):
                return mid
            elif(mid!=len(nums)-1 and nums[mid+1]>nums[mid]):
                low=mid+1
            else:
                high=mid-1
        return -1