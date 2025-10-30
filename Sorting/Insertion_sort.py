def insertion_sort(lst):
 # insertion sort, picks one element and puts it in right place
 for i in range(1, len(lst)):
  key = lst[i]
  j = i - 1
  
  # move stuff bigger than key one step ahead
  while j >= 0 and lst[j] > key:
   lst[j + 1] = lst[j]
   j -= 1
  
  lst[j + 1] = key
  
  # one pass done, moves on
 return lst


if __name__ == "__main__":
 nums = [9,3,57,12,97,36,45,2,27,79]
 print("Before:", nums)
 print("sorting...")

 sorted_nums = insertion_sort(nums)

 print("After :", sorted_nums)
