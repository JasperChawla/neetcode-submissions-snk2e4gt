class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right= len(height)-1
        maxwater=0
        leftmx= height[left]
        rightmx = height[right]
        while left<right:
            if height[left]>height[right]:
                rightmx=max(rightmx,height[right-1])
                maxwater+=(rightmx-height[right-1])*1
                right=right-1   
            else:
                leftmx=max(height[left+1],leftmx)
                maxwater+=(leftmx-height[left+1])*1
                left=left+1 
        return maxwater

           
