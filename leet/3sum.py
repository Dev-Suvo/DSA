class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i,val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1

            while l < r:
                sum3 = val + nums[l] + nums[r]

                if sum3 > 0:
                    r-=1

                elif sum3 < 0:
                    l+=1

                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1

                    while l<r and nums[l] == nums[l+1]:
                        l+=1

        return res