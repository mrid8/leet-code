from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {} # mapping charCount to list of anagrams
        res = defaultdict(list) # to take care of an edge case

        for s in strs: 
            count = [0] * 26 # a...z
            
            for c in s: 
                # count each character in the string by
                # taking the ascii value of the current char by lower "a" 
                # so ex: ord("a") - ord ("a") OR a = 80 -> 0, 80 - 80
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()