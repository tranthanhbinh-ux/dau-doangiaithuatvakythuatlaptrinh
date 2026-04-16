class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        for s in sentences:
            count = len(s.split(" "))
            if count > max_words:
                max_words = count
        
        return max_words
            