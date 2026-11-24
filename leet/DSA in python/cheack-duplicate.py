class Solution(object):
    def containsDuplicate(self, nums):
        map = {}
        
        for n in nums:
            map[n] = map.get(n,0)+1

        for i in map.values():
            if i > 1:
                return True

            return False