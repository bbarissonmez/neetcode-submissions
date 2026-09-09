class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda interval: interval[0])


        removals = 0
        prevEnd = intervals[0][1]

        for i in range (1, len(intervals)):
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]

            if currentStart >= prevEnd:
                # No overlap: keep current interval
                prevEnd = currentEnd
            else:
                # Overlap: count one deletion and keep the earlier ending interval
                removals += 1
                prevEnd = min(prevEnd, currentEnd)

        return removals
        