class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        cnt = 1
        while s != goal:
            s = s[1:] + s[0]
            cnt += 1
            if cnt == len(s):
                break
        return s == goal
