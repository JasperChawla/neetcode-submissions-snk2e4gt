class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        mxarea=0
        while left < right:
            area = ((right-left)*min(heights[left],heights[right]))
            if heights[left] > heights[right]:
                right = right-1

            else:
                 left = left+1
            
            if area > mxarea:
                mxarea = area

        return mxarea