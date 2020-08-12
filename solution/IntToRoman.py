#12. 整数转罗马数字
# 思路一：贪心
# 贪心法则：我们每次尽量使用最大的数来表示。 比如对于 1994 这个数，如果我们每次尽量用最大的数来表示，依次选 1000，900，90，4，会得到正确结果 MCMXCIV。

# 所以，我们将哈希表按照从大到小的顺序排列，然后遍历哈希表，直到表示完整个输入。
def intToRoman(self, num: int) -> str:
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count 
                num %= key
        return res