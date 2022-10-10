class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        first = palindrome[0:n//2]
        second = palindrome[n//2::]
        ans = "z" * n
        
        tmp = list(set(first))
        if len(tmp) == 1 and tmp[0] == "a":
            return first + second[0:-1] + "b"

        for i, c in enumerate(first):
            t = first[0:i] + "a" + first[i+1::]
            if t < ans:
                ans = t
                flag = False
            
        return ans + second