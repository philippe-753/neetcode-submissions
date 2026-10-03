from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_match = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        for par in s:
            if par in par_match:
                stack.append(par)
            else:
                if stack and par == par_match[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        
        return not stack