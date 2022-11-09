class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        last = -1
        if self.stack:
            last = self.stack[-1][1]
        self.stack.append((price, self.day))
        ans = self.day - last
        self.day += 1
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)