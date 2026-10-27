class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False


        smap , tmap = {}, {}

        for i in range(0,len(s)):
            smap[s[i]] = smap.get(s[i],0)+1
            tmap[t[i]] = tmap.get(t[i],0)+1

        return smap == tmap