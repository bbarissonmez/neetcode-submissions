class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n:
            b = n & (~n + 1)
            counter += 1
            n ^= b

        return counter
