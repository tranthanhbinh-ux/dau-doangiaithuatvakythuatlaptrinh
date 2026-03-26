class Solution(object):
    def toGoatLatin(self, sentence):
        nguyenam = "aeiouAEIOU"
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]

            # nguyên âm
            if word[0] in nguyenam:
                new_word = word + "ma"
            else:
                # Phụ âm
                new_word = word[1:] + word[0] + "ma"

            # Thêm 'a' theo vị trí (i + 1)
            new_word += "a" * (i + 1)

            result.append(new_word)

        return " ".join(result)