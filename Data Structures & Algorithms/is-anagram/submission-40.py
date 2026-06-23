class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count={}
        for cha in s:
            count[cha] = count.get(cha, 0) + 1

        for cha in t:
            if cha not in count:
                return False
            count[cha]-=1
            if count[cha]<0:
                return False
        return True
