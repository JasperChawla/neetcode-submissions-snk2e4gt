from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for num, freq in sorted_items[:k]:
            ans.append(num)

        return ans