from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        cnt = Counter()
        paragraph = paragraph.replace('!', ' ').replace('?', ' ').replace('\'', ' ').replace(';', ' ').replace('.',
                                                                                                               ' ').replace(
            ',', ' ')

        print(paragraph)
        paragraph = paragraph.split()
        for i in range(len(paragraph)):
            paragraph[i] = paragraph[i].lower()
            if paragraph[i] not in banned:
                cnt[paragraph[i]] += 1
        return cnt.most_common(1)[0][0]


s = Solution()
print(s.mostCommonWord('a, a, a, a, b,b,b,c, c', ["a"]))
