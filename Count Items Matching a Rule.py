class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        # xác định vị trí
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        
        count = 0
        
        for item in items:
            if item[index] == ruleValue:
                count += 1
        
        return count