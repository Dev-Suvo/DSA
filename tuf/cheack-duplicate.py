class Solution:
    def containsDuplicate(self, nums):
        n = set(nums)
        if len(n) == len(nums):
            return False
        else:
            return True