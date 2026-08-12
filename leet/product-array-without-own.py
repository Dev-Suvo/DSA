class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map =[1]*len(nums)


        prefix= 1
        for i in range(len(nums)):
            map[i] = prefix
            prefix *= nums[i]

        postfix =1
        for i in range(len(nums)-1,-1,-1):
            map[i] *= postfix
            postfix*= nums[i]

        return map