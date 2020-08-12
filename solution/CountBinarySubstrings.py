
## 696. 计数二进制子串
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
# 重复出现的子串要计算它们出现的次数。

def solution(s:str)->int:
    ptr = 0
    last = 0
    ans = 0
    n = len(s)
    while(ptr < n):
        c = s[ptr]
        count = 0
        while(ptr < n and s[ptr] == c):
            ptr = ptr + 1
            count = count + 1
        ans = ans + min(count, last)
        last = count
    return ans

def main():
    print(solution("00110011"))

main()