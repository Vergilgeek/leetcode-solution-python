
# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

from typing import List

# 在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
# 如果它存在，那我们已经找到了对应解，并立即将其返回。
def solution(nums: List[int], target: int) -> List[int]:
    dic = {}
    result = []
    lens = len(nums)
    for i in range(lens):
        a = target - nums[i]
        if a in dic:
            result.append(dic[a])
            result.append(i)
            return result
        else:
            dic[nums[i]] = i
    return result

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = solution(nums, target)
    print(result)


main()