class Solution(object):
    def isValid(self, s):
       stack = []

       cTOs = {
        ")" : "(",
        "}" : "{",
        "]" : "["
       }

       for c in s:
        if c in cTOs:
            if stack and stack[-1] == cTOs[c]:
                stack.pop()

            else:
                return False
        else:
            stack.append(c)

       return True if not stack else False 