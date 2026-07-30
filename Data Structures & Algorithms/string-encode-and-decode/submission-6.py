class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""

        for string in strs:
            n = len(string)
            result += str(n)
            result += "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result: List[str] = []

        str_len = ""
        
        i = 0

        while (i < len(s)):
            if (s[i] != '#'):
                str_len += s[i]

            else: # We are at the delimiter
                result.append(s[i+1:i+1+int(str_len)])
                i += int(str_len)

                str_len = ""

            i += 1
        
        return result
             

