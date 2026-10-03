class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        two, one = cost[0], cost[1]

        for i in range(2, N):
            cur = cost[i] + min(one, two)
            one, two = cur, one

        return min(one, two)