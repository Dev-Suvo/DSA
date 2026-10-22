class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)

        length = 0

        for n in nums:
            if(n-1) not in setnums:
                longest = 0

                while(n+length) in setnums:
                    length +=1

                longest = max(longest,length)

        return longest