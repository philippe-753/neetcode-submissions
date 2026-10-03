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
                if not stack:
                    return False
                last_open = stack.pop()
                if par != par_match[last_open]:
                    return False
        
        
        return not stack