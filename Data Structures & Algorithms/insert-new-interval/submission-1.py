class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        index = 0

        while (index < len(intervals) and intervals[index][1] < newInterval[0]):
            index += 1

        if index == len(intervals):
            intervals.append(newInterval)

        elif intervals[index][0] > newInterval[1]:
            intervals.insert(index, newInterval)

        else:
                i = index
                while i < len(intervals) and newInterval[1] >= intervals[i][0]:
                    newInterval[0] = min(newInterval[0], intervals[i][0])
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    i += 1

                del intervals[index:i]
                intervals.insert(index, newInterval)

        return intervals
                
