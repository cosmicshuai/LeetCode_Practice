#problem link: https://leetcode.com/discuss/interview-question/2535666/Google-or-L5-SDE-or-Assessment-question
import heapq
from collections import  defaultdict
def getDownloadTime(k, dependeny, times):
    indree = defaultdict(int)
    reverseDependency = defaultdict(list)

    for key, v in dependeny.items():
        indree[key] = len(v)
        for j in v:
            reverseDependency[j].append(key)

    t = 0
    processing = []
    canDownload = []
    for key in times.keys():
        if indree[key] == 0:
            heapq.heappush(canDownload, key)
    while True:
        while len(processing) < k and canDownload:
            job = heapq.heappop(canDownload)
            heapq.heappush(processing, (t + times[job], job))

        if processing:
            finish, job = heapq.heappop(processing)
            t = finish
            for nextJob in reverseDependency[job]:
                indree[nextJob] -= 1
                if indree[nextJob] == 0:
                    heapq.heappush(canDownload, nextJob)

        if not canDownload and not processing:
            return t
            

k = 3
times = {"tesla-client": 7, "tesla-common": 3, "tesla-http": 12, "tesla-ui": 10, "juint": 9, "http-client": 11, "tesla-logs": 13, "tesla-grid": 8, "http-core": 5, "tesla-cols": 9, "tesla-rows": 6}
dependeny = {"tesla-client": ["tesla-common", "tesla-http", "tesla-ui"], "tesla-common": ["juint"], "tesla-http": ["http-client", "tesla-logs"], "tesla-ui": ["tesla-grid"], "http-client": ["http-core"], "tesla-grid": ["tesla-cols", "tesla-rows"]}
assert getDownloadTime(k, dependeny, times) == 43