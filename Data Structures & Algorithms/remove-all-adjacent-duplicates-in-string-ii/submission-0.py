class Solution:
    def removeDuplicates(self, s: str, k: int): 
        stack =[] #keep track of char and count

        for ch in s:
            if stack and stack[-1][0]== ch:
                stack[-1][1] +=1

            else:
                stack.append([ch, 1])
            if stack[-1][1] == k:
                stack.pop()

        return ''.join(char * count for char, count in stack)

