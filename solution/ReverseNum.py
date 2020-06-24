# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

def reverse(x: int) -> int:
    INT_MAX = pow(2,31) - 1
    INT_MIN = - pow(2,31)
    rev = 0
    while x!=0:
        if x > 0:
            pop = x%10
            x = x//10
        else:
            pop = x%-10
            x = -(x//-10)
        if rev > INT_MAX/10 or (rev== INT_MAX//10 and pop > 7):
            return 0
        if rev < INT_MIN/10 or (rev == INT_MIN//10 and pop < -8):
            return 0
        rev = rev*10 + pop            
    return rev

def main():
    print(reverse(-123))

main()