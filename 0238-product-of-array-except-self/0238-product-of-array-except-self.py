class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        product = [1] * n
        
        left_product = 1
        for i in range(n):
            product[i] = left_product
            left_product *= nums[i]
            
        right_product = 1
        for i in range(n - 1, -1, -1):
            product[i] *= right_product
            right_product *= nums[i]
            
        return product