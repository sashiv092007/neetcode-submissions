class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxx = 0
        while left < right:
            curr = min(heights[left], heights[right])
            x = right - left
            area = curr * x
            maxx = max(maxx, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxx        