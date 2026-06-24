class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        found =True
        if len(s)!=len(t):
            found=False
            return found
       
        for i in s:
            if s.count(i)!=t.count(i):
                found=False
                break 



        
        return found
                
                