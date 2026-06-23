class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        prvhash={}

        for idx, i in enumerate(nums):
            diff = target - i

            if diff in prvhash:
                return [prvhash[diff], idx]

            prvhash[i]=idx