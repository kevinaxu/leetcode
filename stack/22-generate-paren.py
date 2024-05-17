class Solution:
    def generateParenthesis(self, n):

        stack = ["()"]
        while n > 1:
            combos = set()
            for s in stack:
                combos.add("()" + s)
                combos.add("(" + s + ")")
                combos.add(s + "()")
            stack = list(combos)

            n -= 1

        return stack
        

expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

n = 4
print(Solution().generateParenthesis(n))