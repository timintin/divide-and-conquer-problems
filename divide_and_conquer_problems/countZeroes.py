def countZeroes(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            if mid == 0 or arr[mid - 1] == 1:
                return len(arr) - mid
            right = mid - 1
        else:
            left = mid + 1
    return 0

# Test cases
print(countZeroes([1, 1, 1, 1, 0, 0])) # 2
print(countZeroes([1, 0, 0, 0, 0]))    # 4
print(countZeroes([0, 0, 0]))          # 3
print(countZeroes([1, 1, 1, 1]))       # 0
