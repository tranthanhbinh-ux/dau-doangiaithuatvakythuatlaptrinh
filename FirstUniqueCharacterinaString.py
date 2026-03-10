class Solution(object):
    def firstUniqChar(self, s):
        dem = {}
        for c in s:
            dem[c] = dem.get(c, 0) + 1
        for i in range(len(s)):
            if dem[s[i]] == 1:
                return i
        return -1