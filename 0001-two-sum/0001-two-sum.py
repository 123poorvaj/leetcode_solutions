class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target=target
        for i in range(0,len(nums)):
            targe=target-nums[i]
            for j in range(0,len(nums)):
                if targe==nums[j] and i!=j:
                    return [i,j]
       
