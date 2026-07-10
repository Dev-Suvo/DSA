class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       map = {}

       frq = [[]for _ in range(len(nums)+1)]

       for n in nums:
        map[n] = map.get(n,0)+1

       for c,v in map.items():
        frq[v].append(c)

       res = []

       for i in range(len(frq)-1,0,-1):
        for n in frq[i]:
            res.append(n)
            if len(res) == k:
                return res