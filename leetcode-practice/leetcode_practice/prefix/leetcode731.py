from sortedcontainers import SortedDict

class Solution:
    class MyCalender2:

        def __init__(self):
            self.bookings = SortedDict()

        def book(self, start_time: int, end_time: int) -> bool:
            self.bookings[start_time] = self.bookings.get(start_time, 0) + 1
            self.bookings[end_time] = self.bookings.get(end_time, 0) - 1

            event_counts = 0

            for count in self.bookings.values():
                event_counts += count
                if event_counts > 2:
                    # rollback the intervals that just added
                    self.bookings[start_time] -= 1
                    if self.bookings[start_time] == 0:
                        self.bookings.pop(start_time)

                    self.bookings[end_time] += 1
                    if self.bookings[end_time] == 0:
                        self.bookings.pop(end_time)
                    return False
            
            return True
    