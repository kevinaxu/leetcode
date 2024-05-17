class Solution:
    def evalRPN(self, tokens):
        if len(tokens) == 1:
            return tokens[0]

        stack = []
        for t in tokens:
            if t in ["+", "-", "/", "*"]:
                a = int(stack.pop())
                b = int(stack.pop())

                if t == "/":
                    stack.append(str(int(b/a)))
                elif t == "+":
                    stack.append(str(b + a))
                elif t == "-":
                    stack.append(str(b - a))
                else:
                    stack.append(str(b * a))
            else:
                stack.append(t)


        return int(stack[0])

# tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]

print(Solution().evalRPN(tokens))