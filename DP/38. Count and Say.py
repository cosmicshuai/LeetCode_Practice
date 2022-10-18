class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(s):
            n = len(s)
            prev = s[0]
            cnt = 1
            ans = ""
            for i in range(1, n):
                if s[i] == prev:
                    cnt += 1
                else:
                   ans += (str(cnt) + prev)
                   prev = s[i]
                   cnt = 1

            ans += (str(cnt) + prev)
            return ans

        ans = "1"
        for i in range(2, n + 1):
            ans = say(ans)
        return ans
