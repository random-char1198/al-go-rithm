def addBinary(self, a: str, b: str) -> str:
    return bin(int(a,2)+int(b,2))[2:]
    #sorry
    #it will return 0b1001, so that's why we are slicing them

    
