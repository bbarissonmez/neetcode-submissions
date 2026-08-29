class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        cache = [None] * len(s)

        def dfs(index):
            if index == len(s):
                return True

            if cache[index] is not None:
                return cache[index]

            for end in range(index + 1, len(s) + 1):
                word = s[index:end]

                if word in word_set and dfs(end):
                    cache[index] = True
                    return True

            cache[index] = False
            return False

        return dfs(0)