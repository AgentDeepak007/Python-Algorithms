def binary_search(lst, left, right, target):
    # normal binary search used inside exponential
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def exponential_search(lst, target):
    # exponential search, finds range then does binary search
    if len(lst) == 0:
        return None

    if lst[0] == target:
        return 0

    i = 1
    # keep doubling until we go past or find something close
    while i < len(lst) and lst[i] <= target:
        i = i * 2

    # now do binary search in the found range
    return binary_search(lst, i // 2, min(i, len(lst) - 1), target)


if __name__ == "__main__":
    nums = sorted([9, 3, 57, 12, 97, 36, 45, 2, 27, 79])
    print("Searching in:", nums)

    x = int(input("Enter number to find: "))
    res = exponential_search(nums, x)

    if res != None:
        print("Found at index", res)
    else:
        print("Not found :(")
