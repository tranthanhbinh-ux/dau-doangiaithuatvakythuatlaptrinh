class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        chuoi = ""
        count = 0

        for i in range(len(s) - 1, -1, -1):
            chuoi = s[i] + chuoi
            count += 1
            
            if count == 3 and i != 0:
                chuoi = "." + chuoi
                count = 0

        return chuoi