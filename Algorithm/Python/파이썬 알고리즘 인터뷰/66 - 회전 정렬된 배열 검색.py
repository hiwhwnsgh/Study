from typing import List
def search(nums : List[int], target : int) -> int:
    # 예외처리
    if not nums:
        return -1
    
    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left+(right-left)//2
        print(mid, left, right)
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    pivot = left

    # 피벗 기준 이진 검색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1

nums = [1,2,3,4,5,7,6]
target = 1
print(search(nums,target))