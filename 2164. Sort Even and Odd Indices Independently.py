class Solution(object):
    def sortEvenOdd(self, nums):
        chan = []
        le = []
        
        # Bước 1: tách chẵn và lẻ
        for i in range(len(nums)):
            if i % 2 == 0:
                chan.append(nums[i])
            else:
                le.append(nums[i])
        
        # Bước 2: sort
        chan.sort()                  # tăng dần
        le.sort(reverse=True)       # giảm dần
        
        # Bước 3: ghép lại
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = chan[e]
                e += 1
            else:
                nums[i] = le[o]
                o += 1
        
        return nums