class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        counts = {}
        for i in nums:
            if i in counts:
                return True
            else:
                counts[i] = 1
        
        return False

