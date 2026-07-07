class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash = {}

       for idx, val in enumerate(nums):
            dif = target - val

            if dif in hash:
                return [idx, hash[dif]]

            hash[val] = idx