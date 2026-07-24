class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)        # « transforme nums en sac magique »
        while len(self.heap) > k:       # « tant qu'il y a plus de k nombres dans le sac...
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  # « jette le nouveau nombre dans le sac »
        if len(self.heap) > self.k:     # « le sac contient k+1 nombres, un de trop...
            heapq.heappop(self.heap)    #   ...sors le plus petit et jette-le »
        return self.heap[0]


    

        
