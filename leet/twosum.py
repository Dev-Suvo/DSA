class Solution(object):
    def twoSum(self, nums, target):
        ls = {}
        for i,n in enumerate(nums):
            need = target-n
            if need in ls:
                return [ls[need],i]

            ls[n] = i