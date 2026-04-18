class Solution(object):
    def pickGifts(self, gifts, k):
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)   # lấy max
            new_val = int(math.sqrt(largest))
            heapq.heappush(heap, -new_val)

        return -sum(heap)