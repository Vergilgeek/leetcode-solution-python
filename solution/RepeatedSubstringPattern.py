# 459. 重复的子字符串
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
class Solution:
# 字符串匹配
# 思路与算法:
# 我们可以把字符串 ss 写成 s's'的形式，
# 但我们如何在不枚举 n的情况下，判断 ss 是否能写成上述的形式呢？
# 如果我们移除字符串 ss 的前 n'个字符（即一个完整的 s'），再将这些字符保持顺序添加到剩余字符串的末尾，那么得到的字符串仍然是 ss。
# 那么如果将两个 ss 连在一起，并移除第一个和最后一个字符，那么得到的字符串一定包含 ss，即 ss 是它的一个子串。
# 因此我们可以考虑这种方法：我们将两个 ss 连在一起，并移除第一个和最后一个字符。如果 ss 是该字符串的子串，那么 ss 就满足题目要求。
# 注意到我们证明的是如果 ss 满足题目要求，那么 ss 有这样的性质，而我们使用的方法却是如果 ss 有这样的性质，那么 ss 满足题目要求。
# 因此，只证明了充分性是远远不够的，我们还需要证明必要性。
# https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
# 证明需要使用一些同余运算的小技巧，可以见方法三之后的「正确性证明」部分。
# 这里先假设我们已经完成了证明，这样就可以使用非常简短的代码完成本题。在下面的代码中，我们可以从位置 1 开始查询，并希望查询结果不为位置 n，这与移除字符串的第一个和最后一个字符是等价的。
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)