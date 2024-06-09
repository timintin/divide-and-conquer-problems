def sortedFrequency(arr, num):
    def findFirstOccurrence(arr, num):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                if mid == 0 or arr[mid - 1] < num:
                    return mid
                right = mid - 1
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findLastOccurrence(arr, num):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                if mid == len(arr) - 1 or arr[mid + 1] > num:
                    return mid
                left = mid + 1
            elif arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    first = findFirstOccurrence(arr, num)
    if first == -1:
        return -1
    last = findLastOccurrence(arr, num)
    return last - first + 1

# Test cases
print(sortedFrequency([1,1,2,2,2,2,3], 2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3], 3)) # 1
print(sortedFrequency([1,1,2,2,2,2,3], 1)) # 2
print(sortedFrequency([1,1,2,2,2,2,3], 4)) # -1
