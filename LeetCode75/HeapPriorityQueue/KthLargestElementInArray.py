import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priority_queue = []
        for num in nums:
            if len(priority_queue) < k:
                heapq.heappush(priority_queue, num)
            else:
                heapq.heappush(priority_queue, num)
                heapq.heappop(priority_queue)

        return heapq.heappop(priority_queue)
