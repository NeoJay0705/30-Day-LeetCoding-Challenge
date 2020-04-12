from .maxProfit import printResult
from heapq import heappush, heappop

class Solution:
    @printResult
    def lastStoneWeight(self, stones: list) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -1 * stone)
        
        while len(heap) > 1:
            max1 = heappop(heap)
            max2 = heappop(heap)

            if max1 != max2:
                gap = max1 - max2
                heappush(heap, gap)

        return 0 if len(heap) == 0 else -1 * heap[0]
        
if __name__ == '__main__':
    scanner = Solution()
    scanner.lastStoneWeight([2,7,4,1,8,1])
    scanner.lastStoneWeight([3, 1])
    scanner.lastStoneWeight([2, 2])
    scanner.lastStoneWeight([4,3,4,3,2])
    scanner.lastStoneWeight([8,8,2,1,4,10,8,3])
