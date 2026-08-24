class Solution:
    def numDecodings(self, s: str) -> int:
        counter = 0
        BORDER = len(s)
        cache = [-1] * len(s)

        def dfs(index):
            if index == BORDER:
                return 1

            if s[index] == "0":
                return 0

            if cache[index] == -1:
                if int(s[index:index+2]) <= 26 and index < BORDER - 1:
                    cache[index] = dfs(index + 1) + dfs(index + 2)
                else:
                    cache[index] = dfs(index+1)
            
            return cache[index]

        return dfs(0)


        

    
    def map(self, s:str) -> str:
        return chr(int(s) + 64)
        