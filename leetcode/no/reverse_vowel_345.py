class Solution:
    def isVowel(self, ch: str):
        return ch in 'aeiouAEIOU'

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < n and not self.isVowel(s[left]):
                left += 1
            while right > 0 and not self.isVowel(s[right]):
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
