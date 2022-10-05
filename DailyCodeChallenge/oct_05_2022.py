# 811

from collections import defaultdict, Counter


# how to iterate a default dic?

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        cnt = Counter()
        print(cnt)
        for domain in cpdomains:
            c, s = domain.split()
            c = int(c)
            cnt[s] += c
            print(cnt)
            while '.' in s:
                s = s[s.index('.')+1:]
                cnt[s] += c
        return [f"{c} {s}" for s, c in cnt.items()]


solution = Solution()
print(solution.subdomainVisits(["9001 discuss.leetcode.com"]))
