class Solution:
    def findRelativeRanks(self, score):
        dic, res = {}, []
        res = ["-1"] * len(score)
        for i in range(len(score)):
            dic[score[i]] = i
        score = sorted(score)
        print(dic)
        for i in range(len(score)):
            if i == len(score) - 1:
                res[dic[score[i]]] = "Gold Medal"
            elif i == len(score) - 2:
                res[dic[score[i]]] = "Silver Medal"
            elif i == len(score) - 3:
                res[dic[score[i]]] = "Bronze Medal"
            else:
                res[dic[score[i]]] = str(len(score) - i)
        return res
