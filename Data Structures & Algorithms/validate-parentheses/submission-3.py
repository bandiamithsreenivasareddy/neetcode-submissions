class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid={")":"(","]":"[","}":"{" }
        for p in s:
            if p in valid and stack and stack[-1]==valid[p]:
                stack.pop()
            else:
                stack.append(p)
        return not stack

