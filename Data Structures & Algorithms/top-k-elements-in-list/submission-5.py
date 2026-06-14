from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict(Counter(nums))
        counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
        return list(counts.keys())[:k]
        print(counts)