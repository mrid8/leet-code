from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq = {}
       for i in range(len(nums)):
        if nums[i] in freq > k:
            freq.pop(nums[i])
        freq[nums[i]] += 1
        return freq
