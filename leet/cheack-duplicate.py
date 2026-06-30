class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)

        return not(len(set_num) == len(nums))