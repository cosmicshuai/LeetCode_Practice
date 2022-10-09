class Solution:
    def robotWithString(self, s: str) -> str:
        last = {}
        for i, char in enumerate(s):
            last[char] = i
        
        charset = list(set(s))
        charset.sort(reverse = True)
        ans = ""
        t = []
        curMin = charset.pop()
        for i, char in enumerate(s):
            if char == curMin:
                ans += char
                if i == last[char]:
                    while charset and i > last[charset[-1]]:
                        charset.pop()
                    if not charset: return ans + "".join(t[::-1])
                    curMin = charset.pop()
                    while t and t[-1] <= curMin:
                        ans += t.pop()
            else:
                t.append(char)

        return ans + "".join(t[::-1])