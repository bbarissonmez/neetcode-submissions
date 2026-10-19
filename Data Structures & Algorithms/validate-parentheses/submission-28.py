class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        par = {
            ')':'(', 
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in par:
                if not stack:
                    return False

                last = stack.pop()

                if last != par[char]:
                    return False

            elif char in par.values():
                stack.append(char)

        return not stack

        