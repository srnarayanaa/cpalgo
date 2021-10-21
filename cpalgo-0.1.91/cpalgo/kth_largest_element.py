import heapq
def kth_largest_element(nums, k):
    heap=[]
    for i in nums:
        heapq.heappush(heap,-i)
    for i in range(k):
        res=-heapq.heappop(heap)
    return res