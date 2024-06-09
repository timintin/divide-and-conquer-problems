def findRotatedIndex(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= num < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < num <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Test cases
print(findRotatedIndex([3, 4, 1, 2], 4))        # 1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)) # 2
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndex([37, 44, 66, 102, 10, 22], 14)) # -1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
