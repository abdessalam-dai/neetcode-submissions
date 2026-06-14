class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {x: target - x for x in numbers}
        idx1, idx2 = 0, 0
        for x, y in diffs.items():
            if y in numbers:
                idx1 = numbers.index(x) + 1
                idx2 = numbers.index(y) + 1
        return sorted([idx1, idx2])