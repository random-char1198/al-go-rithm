import collections


class Solution:
    def findAnagrams(self, s: str, p: str):
        s_lan, p_lan, res = len(s), len(p), []
        s_count = [0] * 26  # 26 letters in the alphabet
        p_count = [0] * 26

        for i in range(p_lan):
            p_count[ord(p[i]) - ord('a')] += 1
            # [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        left = 0
        for right in range(s_lan):
            current_right = ord(s[right]) - ord('a')
            s_count[current_right] += 1
            print("Current Right: " + str(current_right))  # c => 2, b => 1, a => 0
            while s_count[current_right] > p_count[current_right]:
                current_left = ord(s[left]) - ord('a')  # retrieve index that we are going to shift 's' - 'a' = 2
                s_count[current_left] -= 1
                left += 1  # shift to right by 1
            if right - left + 1 == p_lan:
                # right == 2, left == 0, 2-0+1 == 3 which is equal to length of "p"
                res.append(left)
        return res
        # print(s_count)
        # print(p_count)


solution = Solution()
print(solution.findAnagrams("cbaebabacd", 'abc'))