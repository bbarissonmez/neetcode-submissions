from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        for num, frequency in frequency_map.items():
            buckets[frequency].append(num)

        result = []

        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)

            if len(result) == k:
                return result

        return result


