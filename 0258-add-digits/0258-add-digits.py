class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))!=1):
            sum_=0
            while(num!=0):
                digit=num%10
                sum_+=digit
                num=num//10
            num=sum_

        return num

        