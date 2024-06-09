def findFloor(arr, x):
    left, right = 0, len(arr) - 1
    floor = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    return floor

# Test cases
print(findFloor([1,2,8,10,12,19], 9))  # 8
print(findFloor([1,2,8,10,12,19], 20)) # 19
print(findFloor([1,2,8,10,12,19], 0))  # -1
