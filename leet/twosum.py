class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for idx, val in enumerate(nums):
            need = target- val

            if need in map:
                return [map[need],idx]    
            
            map[val] = idx
