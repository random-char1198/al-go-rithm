class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        t1 = [0] * 26
        t2 = [0] * 26

        for i in range(len(s1)):
            t1[ord(s1[i]) - ord('a')] += 1

        for i in range(l2):
            if i >= l1:
                t2[ord(s2[i - l1]) - ord('a')] -= 1

            t2[ord(s2[i]) - ord('a')] += 1
            if t1 == t2:
                return True
        return False
