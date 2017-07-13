nums = [10, 9, 1, 7, 2, 6, 5, 4, 3, 0]
nums_small = nums[:4]
nums_empty = []


# bogo sort
def bogo_sort(nums):
    nums = nums[:]
    import random
    l = len(nums)
    while True:
        random.shuffle(nums)
        ordered = True
        for i in range(1, l):
            if nums[i - 1] > nums[i]:
                ordered = False
        if ordered:
            break
    return nums


print('bogo_small: ', bogo_sort(nums_small))


# bubble sort
def bubble_sort(nums):
    nums = nums[:]
    l = len(nums)
    for i in range(l - 1):
        for j in range(1, l - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1:j + 1] = nums[j], nums[j - 1]
    return nums


print('bubble: ', bubble_sort(nums))
print('bubble_small: ', bubble_sort(nums_small))


# insertion sort
def insertion_sort(nums):
    nums = nums[:]
    l = len(nums)
    for i in range(1, l):
        cur = nums[i]
        for j in range(i, -1, -1):
            if nums[j - 1] <= cur:
                break
            nums[j] = nums[j - 1]
        nums[j] = cur
    return nums


print('insertion_small:', insertion_sort(nums_small))
print('insertion:', insertion_sort(nums))


# merge sort
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    split = len(nums) // 2
    sorted_left = merge_sort(nums[:split])
    sorted_right = merge_sort(nums[split:])
    big, small = (sorted_left, sorted_right) if len(sorted_left) > len(sorted_right) else (sorted_right, sorted_left)
    merged = []
    b, s = 0, 0
    while b < len(big) and s < len(small):
        if small[s] <= big[b]:
            merged.append(small[s])
            s += 1
        else:
            merged.append(big[b])
            b += 1
    if b == len(big) and s == len(small):
        return merged
    else:
        if b != len(big):
            merged = [*merged, *big[b:]]
        else:
            merged = [*merged, *small[s:]]
        return merged


print('merge_small', merge_sort(nums_small))
print('merge', merge_sort(nums))

















