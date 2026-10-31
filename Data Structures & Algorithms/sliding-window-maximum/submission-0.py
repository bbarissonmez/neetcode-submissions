class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            if i >= k-1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                result.append(-max_heap[0][0])

        return result


        