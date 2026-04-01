class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right= len(height)-1
        maxwater=0
        leftmx= height[left]
        rightmx = height[right]
        while left<right:
            if height[left]>height[right]:
                if height[right-1]>rightmx:
                    rightmx=height[right-1]
                else:
                    area = (rightmx-height[right-1])*1
                    maxwater+=area
                right=right-1   
            else:
                if height[left+1]>leftmx:
                    leftmx=height[left+1]
                else:
                    area = (leftmx-height[left+1])*1
                    maxwater+=area
                left=left+1 
        return maxwater

           
