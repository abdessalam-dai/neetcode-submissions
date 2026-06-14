class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(token)
            else:
                print(token)
                b = stack.pop()
                a = stack.pop()
                result = eval(f"{a}{token}{b}")
                result = int(result)
                # print(eval(f"{a}{token}{b}"))
                stack.append(result)

        return int(stack.pop())