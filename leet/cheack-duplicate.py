class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set_num = set(nums)

        # return not(len(set_num) == len(nums))

        hash = {}

        for n in nums:
            hash[n] = hash.get(n,0) +1

        for val in hash.values():
            if val > 1 :
                return True
        return False