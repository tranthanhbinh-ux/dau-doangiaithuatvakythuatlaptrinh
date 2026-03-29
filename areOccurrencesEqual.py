class Solution(object):
    def areOccurrencesEqual(self, s):
        dem = {}
        # đếm ký tự
        for ch in s:
            dem[ch] = dem.get(ch, 0) + 1
        # lấy danh sách tần suất
        values = list(dem.values())

        # kiểm tra tất cả có bằng nhau không
        return all(v == values[0] for v in values)
        