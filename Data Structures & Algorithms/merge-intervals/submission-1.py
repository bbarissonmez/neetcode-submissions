class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        print(intervals)
        result = []

        i = 0
        j = i+1

        while (i < len(intervals) and j < len(intervals) + 1):
            if j == len(intervals):
                result.append(intervals[i])

            elif intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])

            else:
                result.append(intervals[i])
                i = j

            j += 1

        return result

        
        