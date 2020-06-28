 # 209. 长度最小的子数组
 # 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
 #
 # 示例: 
 #
 # 输入: s = 7, nums = [2,3,1,2,4,3]
 # 输出: 2
 # 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

from typing import List

## 双指针+动态窗口
def solution(s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    length = len(nums)
    result = length + 1
    idx1 = 0
    idx2 = 0
    total = 0
    while idx1 < length :
        total += nums[idx1]
        while total >= s :
            result = min(result, idx1 - idx2 + 1)
            total -= nums[idx2]
            idx2 = idx2 + 1
        idx1 = idx1 + 1
    return 0 if result == length + 1 else result

def main():
    s = 3
    nums = [1,1]
    print(solution(s, nums))

main()