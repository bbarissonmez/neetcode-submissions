class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k must be between 1 and the max element in piles

        l = 1
        r = max(piles)

        while (l <= r):
            k = l + (r - l) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            # If this k is in the valid range, set the right boundary to k
            if hours <= h:
                if (l == r):
                    return r
                r = k
            else:  # If this k is not valid, we have to set the left boundary to k+1
                l = k+1

            