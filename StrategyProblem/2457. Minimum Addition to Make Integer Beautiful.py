class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        s = str(n)
        tot = sum([int(i) for i in s])
        if tot <= target:
            return 0

        t = []
        s = list(s[::-1]) + ["0"]
        l = len(s)
        i = 0
        while i <= l - 1:
            if tot <= target:
                t += s[i::]
                break
            else:
                tot -= int(s[i])
                t.append("0")
                while s[i + 1] == "9":
                    s[i + 1] = "0"
                    t.append("0")
                    tot -= 9
                    i += 1
                tot += 1
                s[i+1] = str(int(s[i + 1]) + 1)
                i += 1
        ans = int("".join(t[::-1]))
        return ans - n

S = Solution()
a = 8
t = 2
print(S.makeIntegerBeautiful(a, t))