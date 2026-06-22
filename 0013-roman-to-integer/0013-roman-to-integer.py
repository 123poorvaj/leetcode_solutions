class Solution:
    def romanToInt(self, s: str) -> int:
        disc = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n=len(s)
        total=disc[s[n-1]]
        for i in range(n-1,0,-1):
            j=i-1
            if disc[s[j]]<disc[s[i]]:
                total-=disc[s[j]]
            else:
                total+=disc[s[j]]
        return total