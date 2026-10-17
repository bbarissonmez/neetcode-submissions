from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            alph = [0] * 26
            for char in word:
                alph[ord(char) - ord('a')] += 1

            key = tuple(alph)
            groups[key].append(word)

        return list(groups.values())