from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### naive solution
        
        # counts = dict(Counter(nums))
        # counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
        # return list(counts.keys())[:k]
        # print(counts)


        ### bucket sort algorithm
        buckets = [[] for _ in range(len(nums) + 1)]
        n = len(nums)

        counts = dict(Counter(nums))
        for x, count in counts.items():
            buckets[count].append(x)
        
        
        result = []
        for i in range(n, -1, -1):
            bucket = buckets[i]
            result += bucket
        return result[:k]



        
