class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_of_odd=sum([i+i-1 for i in range(1,n+1)])
        sum_of_even=sum([i+i for i in range(1,n+1)])
        a=sum_of_odd
        b=sum_of_even
        gcd=0
        while(a!=0 and b!=0):
            if a>=b:
                a=a%b
            else:
                b=b%a
        gcd=a if a!=0 else b
        return gcd  