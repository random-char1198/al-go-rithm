from collections import defaultdict


class Solution:
    def __init__(self):
        self.res = []
        self.table = []
        self.dic = defaultdict(list)

    def convert_to_ord(self, word):
        res = [0] * 26
        for i in range(len(word)):
            res[ord(word[i]) - ord('a')] += 1
        # print(word, res)
        return res

    def findAnagrams(self, word):
        # first check if the word is already in the table variable.
        table = self.convert_to_ord(word=word)
        str_table = [str(x) for x in table]
        # print(table)
        if table in self.table:
            # print(str_table)
            self.dic[tuple(table)].append(word)
        else:
            self.table.append(table)
            self.dic[tuple(table)].append(word)
        # print(self.dic)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1 and strs[0] == "":
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]
        for i in range(len(strs)):
            self.findAnagrams(word=strs[i])
        # print(self.dic)
        for _, v in reversed(self.dic.items()):
            # self.res.append(v)
            # print(sorted(v))
            self.res.append(sorted(v))
        # print(self.res)
        # return self.res[::-1]
        print(self.dic)
        return self.res


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in dic:
                dic[key] = [word]
            else:
                dic[key].append(word)
        return list(dic.values())


s = Solution()
s.groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"])
