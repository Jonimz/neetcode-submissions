class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #first the substring has to be with out duokicate characxter that means
        #this can be put in a set

        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res

        