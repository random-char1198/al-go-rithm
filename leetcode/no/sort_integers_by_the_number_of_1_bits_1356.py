import collections

class Solution:
    def sortByBits(self, arr):
        res = []
        dic = collections.defaultdict(list)
        for i in range(len(arr)):
            bi = bin(arr[i])
            count = bi.count('1')
            if count not in dic:
                dic[count] = list()
            dic[count].append(arr[i])
        print(dic)
        keys = sorted(dic.keys())
        for k in keys:
            res += sorted(dic[k])
        return res
