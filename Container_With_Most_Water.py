class Solution:
    def maxArea(self, height: List[int]) -> int:
        container = 0
        left,right = 0,len(height)-1

        while left < right:
            container = max(container,min(height[left],height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return container
