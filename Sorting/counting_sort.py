def counting_sort(lst):
 # counting sort, counts frequency of each element
 if len(lst) == 0:
  return lst

 min_val = min(lst)
 max_val = max(lst)
 range_of_elements = max_val - min_val + 1

 count = [0] * range_of_elements
 output = [0] * len(lst)

 # count each element
 for num in lst:
  count[num - min_val] += 1

 # cumulative count
 for i in range(1, range_of_elements):
  count[i] += count[i - 1]

 # place elements in output (reverse for stability)
 for i in range(len(lst) - 1, -1, -1):
  output[count[lst[i] - min_val] - 1] = lst[i]
  count[lst[i] - min_val] -= 1

 # copy back
 for i in range(len(lst)):
  lst[i] = output[i]

 return lst


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:", nums)
 print("sorting...")

 sorted_nums = counting_sort(nums)

 print("After :", sorted_nums)
