def binary_search(arr, val):
    start_pos = 0
    end_pos = len(arr)-1
    while start_pos <= end_pos:
        mid_point = start_pos + (end_pos - start_pos) // 2
        mid_val = arr[mid_point]
        if mid_val == val:
            return mid_point

        if val < mid_val:
            end_pos = mid_point + 1

        else:
            start_pos = mid_point + 1

    return -1

print(binary_search(list(range(100)), 67))