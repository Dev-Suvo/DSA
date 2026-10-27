class Solution(object):
    def groupAnagrams(self, strs):
        map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            map[key].append(s)

        return list(map.values())