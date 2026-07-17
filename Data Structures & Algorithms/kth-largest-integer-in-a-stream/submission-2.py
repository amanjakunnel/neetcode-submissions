import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.h = k, nums[:k]
        heapq.heapify(self.h)
        for i in range(k, len(nums)):
            heapq.heappushpop(self.h, nums[i])

    def add(self, val: int) -> int:
        if len(self.h) == self.k - 1:
            heapq.heappush(self.h, val)
        else:
            heapq.heappushpop(self.h, val)
        return self.h[0]