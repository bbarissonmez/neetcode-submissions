class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n
        monotonic_stack = []

        for i in range (n-1, -1, -1):
            while (monotonic_stack and monotonic_stack[-1][0] <= temperatures[i]):
                monotonic_stack.pop()

            if monotonic_stack:
                result[i] = monotonic_stack[-1][1] - i

            monotonic_stack.append([temperatures[i],i])

        return result
        