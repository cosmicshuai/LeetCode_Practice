class Solution:
    def makeGood(self, s: str) -> str:
        def isBad(c1, c2):
            print(c1, c2, ord(c1), ord(c2))
            return abs(ord(c1) - ord(c2)) == 32

        while True:
            n = len(s)
            t = ""
            i = 0
            while i < n - 1:
                if isBad(s[i], s[i+1]):
                    i += 2
                else:
                    t += s[i]
                    i += 1
            if i == n - 1:
                t += s[i]

            if s == t:
                break
            s = t
        
        return t

a = "leEeetcode"
S = Solution()
print(S.makeGood(a))