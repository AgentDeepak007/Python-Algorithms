def bubble_sort(lst):
 # bubble sort, keeps swapping untill list is sorted
 n = len(lst)
 
 for i in range(n-1):
  for j in range(n-i-1):
   if lst[j] > lst[j+1]:
    # swap em
    lst[j], lst[j+1] = lst[j+1], lst[j]
 
  # pass done
  # decrases range each time
 
 return lst


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:",nums)
 print("sorting...")

 sorted_nums=bubble_sort(nums)

 print("After :",sorted_nums)
