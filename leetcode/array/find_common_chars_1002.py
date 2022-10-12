from collections import Counter


class Solution:

    def commonChars(self, words: list[str]) -> list[str]:
        res = None
        for i in range(len(words)):
            c = Counter(words[i])
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())
