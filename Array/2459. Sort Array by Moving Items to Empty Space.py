from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> int:
        def processZeroAtHead(arr):
            mem = {v: i for i, v in enumerate(arr)}
            #for 0 at head nums[i] should be i, mem[i] = i
            cnt = [0]
            cur = 1 # start from 1 since 0 is at head
            # swap any nums[idx] with nums[mem[0]]
            def swap(idx):
                idx0 = mem[0]
                val = arr[idx]
                arr[idx0], arr[idx] = val, 0
                mem[0], mem[val] = idx, idx0
                cnt[0] += 1

            while True:
                if mem[0] != 0:
                    t = mem[mem[0]]
                    swap(t)
                else:
                    while cur < len(arr) and arr[cur] == cur:
                        cur += 1
                    if cur == len(arr):
                        return cnt[0]
                    swap(mem[arr[cur]])
            

        def processZeroAtTail(arr):
            mem = {v: i for i, v in enumerate(arr)}
            #for 0 at tail, nums[i] should be i - 1, mem[i] = i + 1 
            cnt = [0]
            cur = 0 # start from 0 since 0 is at tail

            # swap any nums[idx] with nums[mem[0]]
            def swap(idx):
                idx0 = mem[0]
                val = arr[idx]
                arr[idx0], arr[idx] = val, 0
                mem[0], mem[val] = idx, idx0
                cnt[0] += 1

            while True:
                if mem[0] != len(arr) - 1:
                    t = mem[mem[0] + 1]
                    swap(t)
                else:
                    while cur < len(arr) and arr[cur] == cur + 1:
                        cur += 1
                    if cur == len(arr) - 1:
                        return cnt[0]
                    swap(mem[arr[cur]])

        return min(processZeroAtHead(nums[:]), processZeroAtTail(nums[:]))
            
S = Solution()
a = [4,2,0,3,1]
print(S.sortArray(a))