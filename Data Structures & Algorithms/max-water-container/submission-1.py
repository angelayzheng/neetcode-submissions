class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_water = 0

        while l < r:
            water = (r - l) * min(heights[l], heights[r])

            if water > max_water:
                max_water = water

            if heights[l] <= heights[r]:
                prev_l = heights[l]
                l += 1

                while l < r and heights[l] <= prev_l:
                    l += 1

            else:
                prev_r = heights[r]
                r -= 1

                while l < r and heights[r] <= prev_r:
                    r -= 1

        return max_water