# 27. 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

def solution1(nums, val):
    l = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l] = nums[i]
            l = l + 1
    return l

def main():
    nums=[3,2,2,3]
    val = 3
    print(solution1(nums, val))

main()