# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"

from typing import List

def commonPrefix(srtA : str, strB : str ):
    count = min(len(srtA), len(strB))
    result = ""
    for i in range(count):
        if srtA[i] == strB[i] :
            result = result + srtA[i]
        else:
            return result
    return result

def soulution1(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    cp = commonPrefix(strs[0], strs[1])
    i = 2
    while i < len(strs):
        cp = commonPrefix(cp, strs[i])
        i = i + 1
    return cp

def mian():
   param =   ["aca","cba"]
   print(soulution1(param))

mian()
