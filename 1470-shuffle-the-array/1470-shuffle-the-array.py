class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        arr2=[]
        arr3=[]
        n=len(nums)
        i=0
        while(i<(n/2)):
            arr.append(nums[i])
            i+=1
        while(i<(n)):
            arr2.append(nums[i])
            i+=1
        i=0
        while i<(n/2):
            arr3.append(arr[i])
            arr3.append(arr2[i])
            i+=1
        return arr3