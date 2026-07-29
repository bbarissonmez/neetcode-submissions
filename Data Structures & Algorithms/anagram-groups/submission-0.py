from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(1) bucket creation
        anagram_dict = defaultdict(list)
        
        for string in strs:

            count = [0] * 26  
            
            for char in string:
                count[ord(char) - ord('a')] += 1
                
            # Convert to tuple for a linear-time hashable key
            anagram_dict[tuple(count)].append(string)
            
        return list(anagram_dict.values())
