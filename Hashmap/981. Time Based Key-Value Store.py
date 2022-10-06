from collections import defaultdict
import bisect


"""
idea: use a haspmap to memorize all timestamps set for a given key, keeps in increasing order
use key + timestamp as new key in another hashmap to memorize all values
using binary search to find the largest timestamp during get method
"""
class TimeMap:
    def __init__(self):
        self.keyTimeMap = defaultdict(list)
        self.valueMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        tmp = self.keyTimeMap[key]
        bisect.insort(tmp, timestamp)
        newKey = key + ":" + str(timestamp)
        self.valueMap[newKey] = value

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.keyTimeMap[key], timestamp)
        if idx == 0:
            return ""
        newKey = key + ":" + str(self.keyTimeMap[key][idx - 1])
        return self.valueMap[newKey]