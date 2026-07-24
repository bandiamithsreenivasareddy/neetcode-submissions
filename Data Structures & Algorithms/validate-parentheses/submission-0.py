class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={")":"(","}":"{","]":"["}
        for p in s:
            if p in "({[":
                stack.append(p)
            elif p in match:
                if not stack or stack[-1]!=match[p]:
                    return False
                stack.pop()
        return not stack
                

            
              
        

