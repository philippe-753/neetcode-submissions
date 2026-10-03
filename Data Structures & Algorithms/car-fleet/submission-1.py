from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        pos_spe = [[position[i], speed[i]] for i in range(N)]
        pos_spe.sort(reverse=True)
        stack = []
        for pos, speed in pos_spe:
            stack.append((target-pos)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() 
            
        return len(stack)
