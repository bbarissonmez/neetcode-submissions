class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        # Build ordering constraints
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            # Invalid prefix case:
            # ["abc", "ab"]
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    before = word1[j]
                    after = word2[j]

                    # Avoid counting the same edge twice
                    if after not in adj[before]:
                        adj[before].add(after)
                        indegree[after] += 1

                    break

        output = []
        processed = set()

        def dfs(node):
            if node in processed:
                return

            processed.add(node)
            output.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)

        for char in indegree:
            if indegree[char] == 0 and char not in processed:
                dfs(char)

        if len(output) != len(indegree):
            return ""

        return "".join(output)