def selection_sort(lst):
 # selection sort, finds the smallest each time and puts it front
 for i in range(len(lst)):
  min_index = i
  
  for j in range(i+1, len(lst)):
   if lst[j] < lst[min_index]:
    min_index = j

  # swap the found one with current
  lst[i], lst[min_index] = lst[min_index], lst[i]
 
  # one pass done, moves on
 return lst


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:",nums)
 print("sorting...")

 sorted_nums=selection_sort(nums)

 print("After :",sorted_nums)
