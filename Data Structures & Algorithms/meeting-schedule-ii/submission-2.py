"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        meeting_rooms = 0

        transformed = []
        for meeting in intervals:
            transformed.append((meeting.start, 1))
            transformed.append((meeting.end, -1))
        transformed.sort(key = lambda x: (x[0], x[1]))

        curr_rooms = 0
        for t, val in transformed:
            curr_rooms += val
            meeting_rooms = max(meeting_rooms, curr_rooms)

        return meeting_rooms 

        

