class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for n in nums:
            map[n]=map.get(n,0)+1

        for n in map.values():
            if n > 1:
                return True
            return False