class Solution(object):
    def secondHighest(self, s):
        so =set()
        # lấy các chữ số
        for ch in s:
            if ch.isdigit():#hàm lấy chữ số từ 0 tới 9
                so.add(int(ch))
        # nếu ít hơn 2 số khác nhau
        if len(so) < 2:
            return -1
        # sắp xếp giảm dần
        so = list(so)
        so.sort(reverse=True) #reverse=true sắp xếp từ lớn tới nhỏ
        
        return so[1]