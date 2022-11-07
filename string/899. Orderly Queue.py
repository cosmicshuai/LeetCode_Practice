class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:

        def rollingSort(t, k):
            stack = []
            tmp = []
            for i, c in enumerate(t):
                cnt = 0
                while stack and stack[-1][1] > c and cnt < 3:
                    cnt += 1 
                    tmp.append(stack.pop())
                stack.append((i, c))
                while tmp:
                    stack.append(tmp.pop())
            return "".join([i[1] for i in stack])
        
        def backtrack(s, k):
            if k == 0 or s == "":
                return s
            
            n = len(s)
            t = "z"
            idx = -1
            for i in range(n):
                if s[i] <= t:
                    t = s[i]
                    idx = i
            print(rollingSort(s[0:idx], k))
            sp = s[idx::] + rollingSort(s[0:idx], k)
            print(sp)
            return sp[0] + backtrack(sp[1::], k -1)

        return backtrack(s, k)
S = Solution()
a = "xzcbya"
k = 3
print(S.orderlyQueue(a, k))