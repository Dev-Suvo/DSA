class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for idx , val in enumerate(nums):
            diff = target-val

            if diff in map:
                return [idx, map[diff]]

            map[val] =idx    