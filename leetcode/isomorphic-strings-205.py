class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        if len(s) != len(t):
            return False
        if s and not t:
            return False
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = t[i]
                #point s[i] to t[i]
            if t[i] not in dic_t:
                dic_t[t[i]] = s[i]
            if s[i] in dic_s and t[i] != dic_s[s[i]]:
                return False
                # {'f':'d'}, {'f':'e'}=> this will replace the prevous one.
                # f is the key and f is in the dictionary
                # we also want to make sure that we are getting the same thing from 2 dic/
            if t[i] in dic_t and s[i] != dic_t[t[i]]:
                return False
        return True
