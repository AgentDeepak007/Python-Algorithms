def merge_sort(lst):
 # merge sort, devides the list and then combines in sorted way
 if len(lst) <= 1:
  return lst

 mid = len(lst)//2
 left_half = merge_sort(lst[:mid])
 right_half = merge_sort(lst[mid:])
 
 return mergeThem(left_half, right_half)


def mergeThem(a,b):
 result=[]
 i=j=0

 # merging part
 while i < len(a) and j < len(b):
  if a[i] < b[j]:
   result.append(a[i])
   i+=1
  else:
   result.append(b[j])
   j+=1

 # add what’s left from a
 while i < len(a):
  result.append(a[i])
  i+=1

  # add what’s left from b (if any)
 while j < len(b):
   result.append(b[j])
   j+=1

 return result


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Before:",nums)
 print("sorting...")

 sorted_nums=merge_sort(nums)

 print("After :",sorted_nums)
