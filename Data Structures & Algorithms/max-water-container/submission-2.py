class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_surface = 0
        while l < r:
            hl = heights[l]
            hr = heights[r]

            surface = min(hl, hr) * (r - l)
            print(hl, hr, (r-l))
            if surface > max_surface:
                max_surface = surface

            if hl < hr:
                l += 1
            else:
                r -= 1
        return max_surface