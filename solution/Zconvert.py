
# 6. Z 字形变换
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# 
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：

from typing import List

def solution(s: str, numRows: int) -> str:
    m = [numRows][len(s)]
    x = -1; y = 0
    status = 0
    for c in s:
        if status == 0:
            x= x+1
            m[x][y] = c
            if x +1 >= numRows:
                status = 1
        else:
            x=x-1
            y=y+1
            m[x][y] = c
            if x >=0:
                status = 0
    result = ""
    for xArr in m:
        for s in xArr:
            result.join(s)
    return result

def main() -> str:
    s = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.";
    numRows = 2
    return solution(s, numRows)

main()