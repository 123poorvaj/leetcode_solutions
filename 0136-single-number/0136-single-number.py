class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a=nums[0]
        for i in range(len(nums)):
            n=nums[i]
            if nums.count(n)<=1:
                a=n
        return a
            