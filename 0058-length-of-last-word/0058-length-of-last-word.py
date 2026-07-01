class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        count=0
        s=s.strip(" ")
        n=len(s)
        i=n-1
        while(i>=0):
            if s[i]!=" ":
                count+=1
            else:
                break
            i-=1
        return count
        