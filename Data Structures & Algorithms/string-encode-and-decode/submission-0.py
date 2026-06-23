class Solution:


    def encode(self, strs: List[str]) -> str:


        res = ""   # general string we are going to return 

        for s in strs:

            res += str(len(s)) + "#" + s

        return res 


    def decode(self, s: str) -> List[str]:

        # the s here represents the list of strings that we want to return 

        final_res = []

        i = 0 

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 

            length = int(s[i:j])

            i = j + 1 

            j = i + length

            final_res.append(s[i : j])
            # let's continue our iteration
            i = j

        return final_res

