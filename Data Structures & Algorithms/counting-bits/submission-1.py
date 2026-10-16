class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range (0, n+1):
            bits = 0
            while i:
                i &= i-1
                bits +=1
            result.append(bits)

        return result
