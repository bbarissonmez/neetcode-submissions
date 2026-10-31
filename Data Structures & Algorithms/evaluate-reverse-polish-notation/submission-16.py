from math import ceil, floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+": lambda x, y : x + y,
        "-": lambda x, y : x - y, 
        "*": lambda x, y : x * y,
        "/": lambda x, y : floor(x / y) if x / y > 0 else ceil(x/y)
        }

        stack = []

        for i in range (len(tokens)):
            if tokens[i] in op:
                num1 = stack.pop()
                num2 = stack.pop()

                result = op[tokens[i]](num2, num1)
                stack.append(result)

            else:
                stack.append(int(tokens[i]))


        return stack.pop()

