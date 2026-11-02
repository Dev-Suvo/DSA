class Solution(object):
    def twoSum(self, nums, target):
        map ={}

        for i,n in enumerate(nums):
            need = target - n
            
            if need in map:
                return [map[need], i]

            map[n] = i