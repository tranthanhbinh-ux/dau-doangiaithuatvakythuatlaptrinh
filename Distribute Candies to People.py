class Solution(object):
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            # nếu không đủ kẹo thì đưa hết
            if candies < give:
                res[i] += candies
                break
            res[i] += give
            candies -= give
            
            give += 1
            i = (i + 1) % num_people  # quay vòng

        return res