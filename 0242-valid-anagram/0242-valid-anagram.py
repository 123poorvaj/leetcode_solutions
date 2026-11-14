class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[char for char in s]
        l2=[item for item in t]
        l1.sort()
        l2.sort()
        return l1==l2
