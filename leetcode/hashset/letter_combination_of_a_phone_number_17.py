class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digit):
            if len(next_digit) == 0:
                # print(combination)
                res.append(combination)
            else:
                for letter in dic[next_digit[0]]:
                    # print(dic[next_digit[0]])
                    backtrack(combination + letter, next_digit[1:])

        res = []
        backtrack('', digits)
        return res
