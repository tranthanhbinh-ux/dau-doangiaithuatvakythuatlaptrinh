class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            count[charS] = count.get(charS, 0) + 1
            count[charT] = count.get(charT, 0) - 1
        for value in count.values():
            if value != 0:
                return False
        return True