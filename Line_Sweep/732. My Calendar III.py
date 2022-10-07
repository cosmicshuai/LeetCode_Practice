import bisect
class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        bisect.insort_left(self.events, (start, 1))
        bisect.insort_right(self.events, (end, -1))
        ans = 0
        cur = 0
        for eve, t in self.events:
            cur += t
            ans = max(ans, cur)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)