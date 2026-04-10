class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        left.append(1)
        right.append(1)
        ans=[]
        for i in range(1,len(nums)):
            left.append( left[i-1]*nums[i-1])
        for j in range (1,len(nums)):
            right.append(nums[len(nums)-j]*right[j-1])
        for n in range(0,len(nums)):
            ans.append(left[n]*right[len(right)-1-n])
    
        return ans 
        



            

            
        
       