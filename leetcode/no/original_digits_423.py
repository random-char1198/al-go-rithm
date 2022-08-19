class Solution:
    def originalDigits(self, s: str) -> str:
        res = [0] * 10
        print(len(s))
        for c in range(len(s)):
            if s[c] == 'z':  # 0
                res[0] += 1
            if s[c] == 'o':  # 1 0 2 4
                res[1] += 1
            if s[c] == 'w':  # 2
                res[2] += 1
            if s[c] == 'h':  # 3 8
                res[3] += 1
            if s[c] == 'u':  # 4
                res[4] += 1
            if s[c] == 'f':  # 5  4
                res[5] += 1
            if s[c] == 'x':  # 6
                res[6] += 1
            if s[c] == 's':  # 7  6
                res[7] += 1
            if s[c] == 'g':  # 8
                res[8] += 1
            if s[c] == 'i':  # 9 8 5 6
                res[9] += 1
        res[7] -= res[6]
        res[5] -= res[4]
        res[3] -= res[8]
        res[9] = res[9] - res[8] - res[5] - res[6]
        res[1] = res[1] - res[0] - res[2] - res[4]
        print(res)
        d = ''
        for i in range(10):
            d += str(i) * res[i] if res[i] != 0 else ''
        return d


solution = Solution()
print(solution.originalDigits('owoztneoer'))
