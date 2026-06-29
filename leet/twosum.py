class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for idx , i in enumerate(nums):
            need = target - i

            if need in map:
                return [idx, map[need]]

            map[i] = idx    