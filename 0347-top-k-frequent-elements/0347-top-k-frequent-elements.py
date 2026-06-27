from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        heap = []
        
        for key, val in d.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            elif val > heap[0][0]:
                heapq.heapreplace(heap, (val, key))

        return [i[1] for i in heap]