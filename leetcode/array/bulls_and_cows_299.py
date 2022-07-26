from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0,0
        secret_dict = defaultdict(int)
        guess_dict = defaultdict(int)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull+=1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] +=1
        for i in guess_dict:
            cow += min(guess_dict[i],secret_dict[i])
        return f"{bull}A{cow}B"


solution = Solution()
solution.getHint("1807", "7810")
