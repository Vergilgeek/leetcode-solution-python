## 二分查找
from typing import List
def binarySearch(nums: List[int], target: int) -> int:
    low = 0 
    high = len(nums) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return low


nums = [0,1,2,3,4,5,6,7,9]
target = 7
print(binarySearch(nums, target))