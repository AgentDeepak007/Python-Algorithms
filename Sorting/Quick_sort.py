def quick_sort(lst):
 # quick sort, picks a pivot and devides stuff around it
 if len(lst) <= 1:
  return lst

 pivot = lst[len(lst)//2]
 left = [x for x in lst if x < pivot]
 mid = [x for x in lst if x == pivot]
 right = [x for x in lst if x > pivot]

 # recurively sort left and right side
 return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:",nums)
 print("sorting...")

 sorted_nums = quick_sort(nums)

 print("After :",sorted_nums)
