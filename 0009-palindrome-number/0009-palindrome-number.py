class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        while(x>0):
            rimender=x%10
            rev=rev*10+rimender
            x=x//10
        return n==rev
            