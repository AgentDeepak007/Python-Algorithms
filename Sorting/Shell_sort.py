def shell_sort(lst):
 # shell sort, reduces the gap each time
 n = len(lst)
 gap = n // 2

 while gap > 0:
  for i in range(gap, n):
   temp = lst[i]
   j = i
   while j >= gap and lst[j - gap] > temp:
    lst[j] = lst[j - gap]
    j -= gap
   lst[j] = temp

  gap //= 2

 return lst


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:", nums)
 print("sorting...")

 sorted_nums = shell_sort(nums)

 print("After :", sorted_nums)
