class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # checking the base case 

        if t == "": return ""


        countT, window = {}, {} 

        for c in t:

            countT[c] = 1 + countT.get(c,  0)


        res, resLen = [-1, -1], float("infinity")  

        have, need = 0, len(countT)
        l = 0


        for r in range(len(s)):
            # we need to get the character 
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check to see if the actual c element we are dealing with is equal
            if c in countT  and countT[c] == window[c]:
                have += 1


            while have == need:

                if (r -l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                # checking for the actual element
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 
            
                l += 1 

        l, r = res 
        return s[l:r+1] if resLen != float("infinity") else ""
