class Solution:
    def calculate(self, s: str) -> int:
        def isNumber(c):
            return c in "0123456789"
        elements = []
        ops = "+-*/"
        t = ""
        for c in s:
            if t.isnumeric() and isNumber(c):
                t += c
            elif t == " ":
                continue
            else:
                if t != "":
                    elements.append(t)
                t = c
        elements.append(t)
        def operate(stack, op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
       
        def process(eles):
            n = len(eles)
            i = 0
            stack = []
            op = "+"
            cur = 0
            while i < n:
                t = eles[i]
                if t.isnumeric():
                    cur = int(t)
                elif t in ops:
                    operate(stack, op, cur)
                    op = t
                elif t == "(":
                    cur, l = process(eles[i+1::])
                    i += (l + 1)
                elif t == ")":
                    operate(stack, op, cur)
                    return sum(stack), i
                i += 1
            operate(stack, op, cur)
            return sum(stack)
        
        return process(elements)