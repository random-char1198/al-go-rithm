class Solution:
    def findWords(self,words):
        # words = [word.lower() for word in words]
        sequences = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        dic, res = {}, []
        # this for loop basically create a map and map every letter with its corresponding row
        # {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2,
        #  'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        for i in range(len(sequences)):
            if i == 0:
                dic = {x: 1 for x in sequences[0]}
            elif i == 1:
                for ch in sequences[1]:
                    dic[ch] = 2
            else:
                for ch in sequences[2]:
                    dic[ch] = 3
        # Since every letter has its row #
        # Let the sum of all the row # divided by the first index of the letter can tell us if they are in the same row
        for word in words:
            index = word[0].lower()
            flag = 0
            for i in range(len(word)):
                flag += dic[word[i].lower()]
            if flag / len(word) == dic[index]:
                res.append(word)
            else:
                continue
        return res
