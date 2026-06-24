class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frq_s = Counter(s)
        # frq_t = Counter(t)

        # if frq_s == frq_t :
        #     return True

        # return False  

        if len(s) != len(t):
            return False

        countS , countT = {} , {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1

        return countS == countT
        