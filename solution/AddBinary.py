# 67. 二进制求和
 # 给你两个二进制字符串，返回它们的和（用二进制表示）。
 #
 # 输入为 非空 字符串且只包含数字 1 和 0。
 # 示例 1:
 #
 # 输入: a = "11", b = "1"
 # 输出: "100"
 # 示例 2:
 #
 # 输入: a = "1010", b = "1011"
 # 输出: "10101"


def solution(a: str, b: str) -> str:
    la = len(a) -1
    lb = len(b) -1
    carry = 0
    result = []
    while la >=0 or lb>=0 :
        na = 0
        nb = 0
        if la >= 0 :
            na = int(a[la])
        if lb >= 0 :
            nb = int(b[lb])
        sum = na + nb + carry
        curr = int(sum % 2)
        carry = int(sum / 2) 
        result.insert(0, str(curr))
        la=la -1
        lb = lb -1
    if carry > 0:
        result.insert(0, str(carry))
    return "".join(result)
def main():
    a = "0"
    b = "0"
    print(solution(a,b))

main()
