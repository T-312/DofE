# def binary_search(arr, val):
#     arr.sort()
#     start = 0
#     stop = len(arr)-1
#     while start <= stop:
#         mid_point = start + (stop - start) // 2
#         mid_val = arr[mid_point]

#         if val == mid_val:
#             return mid_point

#         if val < mid_val:
#             stop = mid_point+1

#         else:
#             start = mid_point+1

#     return -1

# print(binary_search([1, 43, 23, 54, 55, 22], 22))

# def find_closest(arr, val):
#     arr.sort()
#     arr = arr[arr.index(val)-1:arr.index(val)+2]
#     return arr

multiples = list(range(60, 600, 60))
print(multiples)

def find_closest(arr, val):
    poss = []
    for n in arr:
        poss.append(abs(val-n))

    return val - min(poss)