class Solution:
    def isHappy(self, n: int) -> bool:
        memory=set()
        while(n!=1):
            if n in memory:
                return False
            digit=0
            memory.add(n)
            while(n!=0):
                last_digit=n%10 
                digit+=last_digit**2
                n=n//10
            n=digit
        return True
    
        