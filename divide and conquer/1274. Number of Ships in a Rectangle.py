# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
    pass
#
class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def isSamePoint(self, p1, p2):
        return p1.x == p2.x and p1.y == p2.y

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0

        if self.isSamePoint(topRight, bottomLeft):
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x - bottomLeft.x == 1 and topRight.y - bottomLeft.y == 1:
            p1 = Point(bottomLeft.x, topRight.y)
            p2 = Point(topRight.x, bottomLeft.y)
            return self.countShips(sea, bottomLeft, bottomLeft) + self.countShips(sea, topRight, topRight) + self.countShips(sea, p1, p1) + self.countShips(sea, p2, p2)

        midx = (topRight.x + bottomLeft.x) // 2
        midy = (topRight.y + bottomLeft.y) // 2
        mid = Point(midx, midy)
        p1 = Point(bottomLeft.x, midy + 1)
        p2 = Point(midx, topRight.y)
        p3 = Point(topRight.x, midy)
        p4 = Point(midx + 1, bottomLeft.y)
        p5 = Point(midx + 1, midy + 1)

        return self.countShips(sea, mid, bottomLeft) + self.countShips(sea, p2, p1) + self.countShips(sea, topRight, p5) + self.countShips(sea, p3, p4)
    