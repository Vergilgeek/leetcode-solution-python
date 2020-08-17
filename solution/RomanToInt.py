# 13. 罗马数字转整数
def romanToInt(self, s: str) -> int:
    d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum = 0 
    preNum = d[s[0]]
    for i in range(1,len(s)):
        num = d[s[i]]
        if preNum < num:
            sum -= preNum
        else :
            sum += preNum
        preNum = num
    sum += preNum
    return sum