class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def operate(s, op):
            b = int(s.pop())
            a = int(s.pop())
            t = 0
            if op == "+":
                t = a + b
            elif op == "-":
                t = a - b
            elif op == "*":
                t = a * b
            else:
                t =  a / b
            s.append(int(t))

        for c in tokens:
            if c in "+-*/":
                operate(stack, c)
                
            else:
                stack.append(c)
        return stack[0]