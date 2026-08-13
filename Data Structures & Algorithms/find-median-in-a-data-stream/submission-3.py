import heapq
class MedianFinder:

    def __init__(self):
        self.left_arr = []   
        self.right_arr = []    

    def addNum(self, num: int) -> None:
        if not self.left_arr or num < -self.left_arr[0]:
            heapq.heappush(self.left_arr, -num)
        else:
            heapq.heappush(self.right_arr, num)
            
        if abs(len(self.left_arr) - len(self.right_arr)) > 1:
            if len(self.left_arr) > len(self.right_arr):
                val = -heapq.heappop(self.left_arr)
                heapq.heappush(self.right_arr, val)
            else:
                val = heapq.heappop(self.right_arr)
                heapq.heappush(self.left_arr, -val)

    def findMedian(self) -> float:
        length = len(self.left_arr) + len(self.right_arr)
        if length % 2 == 0:
            return (-self.left_arr[0] + self.right_arr[0]) / 2
        else:
            if len(self.left_arr) > len(self.right_arr):
                return -self.left_arr[0]
            else:
                return self.right_arr[0]
        
        