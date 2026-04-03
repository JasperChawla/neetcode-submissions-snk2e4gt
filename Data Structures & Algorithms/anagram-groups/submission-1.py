class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        
        for word in strs:
            key = "".join(sorted(word))

            if key not in ans:
                ans[key]=[]
            
            ans[key].append(word) 
        l=[]
        for _,val in ans.items():
            l.append(val)
        return  l        



        