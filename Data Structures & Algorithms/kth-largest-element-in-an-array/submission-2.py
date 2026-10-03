import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick sort: O(N) average, worst O(N^2)
        k = len(nums) - k
        def quick_sort(left, right):
            pivot, p = nums[right], left
            # print("pivot:", pivot)
            for i in range(left, right):
                # print("----")
                # print("i:", i)
                # print("p:", p)
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                # print("nums:", nums)

            nums[p], nums[right] = pivot, nums[p]
            
            if p > k: return quick_sort(left, p-1)
            elif p < k: return quick_sort(p+1, right)
            else: return nums[p]
        return quick_sort(0, len(nums)-1)