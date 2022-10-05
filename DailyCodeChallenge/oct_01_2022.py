class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-","").replace(" ",'')
        res = ""
        for i in range(0,len(number),3):
            if len(number[i:]) <= 4:
                if len(number[i:]) == 4:
                    res += number[i:i+2]
                    res += "-"
                    res += number[i+2:]
                elif len(number[i:]) == 3:
                    res += number[i:i+3]
                elif len(number[i:]) == 2:
                    res += number[i:i+2]
                else:
                    print("weird happened")
            else:
                if i + 3 == len(number):
                    res += number[i:i+3]
                else:
                    res += number[i:i+3]
                    res += '-'
        return res
