"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        start_list = [x.start for x in intervals]
        end_list = [x.end for x in intervals]

        start_list.sort()
        end_list.sort()

        s, counter = 0, 0
        meeting_room = 0

        for e in range(len(end_list)):
            while (s < len(intervals) and start_list[s] < end_list[e]):
                s += 1
                counter += 1
        
            meeting_room = max(meeting_room, counter)
            counter -= 1

        return meeting_room

        