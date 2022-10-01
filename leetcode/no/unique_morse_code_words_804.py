class Solution:
    def translate(self,word:str):
        morse_sequence = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        sequence = ""
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            sequence += morse_sequence[index]
        return sequence
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        res = []
        for word in words:
            res.append(self.translate(word))
        return len(set(res))