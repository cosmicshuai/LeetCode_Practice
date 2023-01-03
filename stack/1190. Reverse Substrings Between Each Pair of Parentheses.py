class Solution:
    def reverseParentheses(self, s: str) -> str:
        def dfs(s, dir):
            stack = []
            n = len(s)
            i = 0
            while i < n:
                if s[i] == "(":
                    t, l = dfs(s[i+1::], not dir)
                    stack.append(t)
                    i += (l + 1)
                elif s[i] == ")":
                    if dir:
                        return "".join(stack), i
                    else:
                        return "".join(stack[::-1]), i
                else:
                    stack.append(s[i])
                i += 1
            if dir:
                return "".join(stack)
            else:
                return "".join(stack[::-1])
        return dfs(s, True)


s = "(abcd)"
S = Solution()
print(S.reverseParentheses(s))