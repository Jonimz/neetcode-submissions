class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return sorted(s)== sorted(t)
        elif len(s) != len(t):
            return False
        

        