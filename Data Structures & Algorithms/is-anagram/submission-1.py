class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}

        if len(s) != len(t):
            return False

        for i in s:
            a[i] = a.get(i, 0) + 1

        for j in t:
            a[j] = a.get(j, 0) - 1

        for value in a.values():
            if value != 0:
                return False

        return True