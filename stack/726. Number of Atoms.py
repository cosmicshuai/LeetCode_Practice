class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def isUpper(c):
            return ord("A") <= ord(c) <= ord("Z")
        
        def isLower(c):
            return ord("a") <= ord(c) <= ord("z")
        
        def isNumber(c):
            return c in "01234456789"

        elements = []
        t = ""
        for c in formula:
            if isLower(c):
                t += c
            elif t.isnumeric() and isNumber(c):
                t += c
            else:
                if t != "":
                    elements.append(t)
                t = c
        elements.append(t)

        def expand(dic, x):
            for key in dic.keys():
                dic[key] *= x
        
        def merge(arr):
            ans = {}
            for t in arr:
                for key in t.keys():
                    ans[key] = ans.get(key, 0) + t[key]
            return ans
        
        def process(eles):
            ans = []
            n = len(eles)
            i = 0
            while i < n:
                t = eles[i]
                if t.isnumeric():
                    cur = ans[-1]
                    expand(cur, int(t))
                elif t == "(":
                    temp, l = process(eles[i+1::])
                    ans.append(temp)
                    i += (l + 1)
                elif t == ")":
                    return merge(ans), i
                else:
                    ans.append({t: 1})
                i += 1
            return merge(ans)

        ans = process(elements)
        res = ""
        keys = list(ans.keys())
        keys.sort()
        for k in keys:
            v = ans[k]
            if v == 1:
                res += k
            else:
                res += (k + str(v))
        return res