class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        tmap, smap = {}, {}

        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i],0)+1
            tmap[t[i]] = tmap.get(t[i],0)+1

        return smap == tmap