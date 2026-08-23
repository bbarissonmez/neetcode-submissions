class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adjacency}

        for i in range (len(words) - 1):
            word_one = words[i]
            word_two = words[i+1]

            min_len = min(len(word_one), len(word_two))

            if word_one[:min_len] == word_two[:min_len] and len(word_two) < len(word_one):
                return ""

            for j in range(min_len):
                if (word_one[j] != word_two[j]):
                    if word_two[j] not in adjacency[word_one[j]]:
                        adjacency[word_one[j]].add(word_two[j])
                        indegree[word_two[j]] += 1
                    break


        output = []
        processed = set()

        def dfs(char):
            print(char, adjacency[char])
            processed.add(char)
            output.append(char)

            for nei in adjacency[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0 and nei not in processed:
                    dfs(nei)

        for char, degree in indegree.items():
            if degree == 0 and char not in processed:
                dfs(char)

        if len(output) != len(indegree):
            return ""

        return "".join(output)

