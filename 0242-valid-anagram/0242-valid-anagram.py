class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            l1=sorted([char for char in s])
            l2=sorted([item for item in t])
            return l1==l2
        else:
            return False
