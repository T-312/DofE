# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def func(arr):
    arr.sort()
    for n in arr:
        if n<=0:
            arr.remove(n)

    for i in range(1, arr[-1]+1):
        if i not in arr or i == arr[-1]:
            return i+1

print(func([3, 4, -1, 1]))