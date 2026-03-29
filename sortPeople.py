class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(names, heights))
        # sắp xếp theo height giảm dần
        people.sort(key=lambda x: x[1], reverse=True)
        result = []
        for name, height in people:
            result.append(name)

        return result