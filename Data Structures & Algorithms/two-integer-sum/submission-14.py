class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first solution
        d = {n: target - n for n in nums}
        for n, m in d.items():
            n_index = nums.index(n)
            m_index = nums.index(m) if m in nums else -1
            if n_index == m_index:
                m_index = nums.index(m, m_index+1) if m in nums[n_index+1:] else -1
            if m_index != -1:
                return [n_index, m_index]
        return []