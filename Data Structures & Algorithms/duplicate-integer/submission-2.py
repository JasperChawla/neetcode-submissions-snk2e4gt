class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     lastseen = set()
     for i in nums:
        if i in lastseen:
            return True
        else:
            lastseen.add(i)
     return False
    
