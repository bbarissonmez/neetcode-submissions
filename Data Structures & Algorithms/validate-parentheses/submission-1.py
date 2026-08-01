class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {')': '(', ']':'[', '}': '{'}
        stack = []

        for char in s:
            if char in parantheses.values():
                stack.append(char)

            if char in parantheses.keys():
                if not stack:
                    return False
                matchy_bracy = stack.pop()
                if (not parantheses[char] == matchy_bracy):
                    return False


        return (not stack)

        