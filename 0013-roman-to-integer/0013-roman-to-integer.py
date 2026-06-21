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

        total = 0

        for i in range(len(s) - 1):
            if disc[s[i]] < disc[s[i + 1]]:
                total -= disc[s[i]]
            else:
                total += disc[s[i]]

        total += disc[s[-1]]
        return total