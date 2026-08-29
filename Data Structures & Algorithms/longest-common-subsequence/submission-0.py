class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1) # Rows
        len2 = len(text2) # Cols

        cache = [[None for _ in range(len2)] for _ in range(len1)]
        
        def dfs(index1, index2):
            if index1 >= len1 or index2 >= len2:
                return 0

            if cache[index1][index2] != None:
                return cache[index1][index2]

            if text1[index1] == text2[index2]:
                cache[index1][index2] = 1 + dfs(index1+1, index2+1)
            else:
                str1 = dfs(index1+1, index2)
                str2 = dfs(index1, index2 + 1)
                cache[index1][index2] = max(str1, str2)

            return cache[index1][index2]

        return dfs(0,0)
