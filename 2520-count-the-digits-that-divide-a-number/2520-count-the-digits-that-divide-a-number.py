class Solution:
    def countDigits(self, num: int) -> int:
        num_list=[int(i) for i in str(num)]
        # return num_list
        count=0
        for i in num_list:
            if num%i==0:
                count+=1
        return count