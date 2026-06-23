class Solution:
    def isValid(self, s: str) -> bool:
        valid_para = ['()', '{}','[]'] #store the valid paranthesis in a list
        while any(pair in s for pair in valid_para): #keep looping through as long as there is any valid pair in the string
              for pair in valid_para: #for each pair in valid parenthesis, remove it whenever it appears
                if pair in s:
                    s = s.replace(pair, '') 
        return s == ''#if the string is empty then it is valid



        
        
        