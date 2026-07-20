class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set_num = set(nums)

        # return not(len(set_num) == len(nums))


        map = {}

        for n in nums:
            map[n] = map.get(n,0)+1

        for c in map.values():
            if c > 1:
                return True
        return False