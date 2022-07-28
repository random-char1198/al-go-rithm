class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def s_compare(s: str) -> str:
            res = []
            for i in s:
                if i != "#":
                    res.append(i)
                else:
                    res.pop()
            return "".join(res)

        return s_compare(S) == s_compare(T)
