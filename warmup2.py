def binary_search(arr, val):
    arr.sort()
    start_pos = 0
    end_pos = len(arr) - 1

    while start_pos <= end_pos:
        mid_point = start_pos + (end_pos - start_pos) // 2
        mid_val = arr[mid_point]
        if mid_val == val:
            return mid_point

        if val < mid_val:
            end_pos = mid_point + 1

        else:
            start_pos = mid_point + 1

    return None

print(binary_search([1,2,3,4,5,6,7,8,9], 9))