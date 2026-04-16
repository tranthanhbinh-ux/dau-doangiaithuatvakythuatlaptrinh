def minimumCost(self, cost):
        cost.sort(reverse=True)  # sắp xếp giảm dần
        total = 0

        for i in range(len(cost)):
            # cứ mỗi 3 viên thì bỏ viên thứ 3
            if i % 3 != 2:
                total += cost[i]

        return total