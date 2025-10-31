def ternary_search(lst, target):
    # ternary search, splits list into 3 parts
    left = 0
    right = len(lst) - 1

    while left <= right:
        # find the 2 mid points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # check both mids
        if lst[mid1] == target:
            return mid1
        if lst[mid2] == target:
            return mid2

        # if target is smaller, it lies in left part
        if target < lst[mid1]:
            right = mid1 - 1
        # if target is bigger, it lies in right part
        elif target > lst[mid2]:
            left = mid2 + 1
        # else it lies between mid1 and mid2
        else:
            left = mid1 + 1
            right = mid2 - 1

    # not found anywhere
    return None


if __name__ == "__main__":
    nums = sorted([9, 3, 57, 12, 97, 36, 45, 2, 27, 79])
    print("Searching in:", nums)

    x = int(input("Enter number to find: "))
    res = ternary_search(nums, x)

    if res != None:
        print("Found at index", res)
    else:
        print("Not found :(")
