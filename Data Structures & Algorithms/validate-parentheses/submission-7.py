class Solution:
    def isValid(self, s: str) -> bool:

        # initialize a stack 
        stack = []
        # initailize our dictionary close to Open 
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{'}



        # a for loop to iterate through s 
        for c in s:

            # check to see if it is in our dictionary 
            if c in closeToOpen:

                # check to see if we have our stack and the topmost element of our stack  is equal to the value in our dictionary
                if stack and stack[-1] == closeToOpen[c]:
                    print(closeToOpen[c])
                    stack.pop()


                    # else we return False
                else:
                    return False

                # else we add it to our stack 
            else:
                stack.append(c)

        # return True 
        return True if not stack else False






        