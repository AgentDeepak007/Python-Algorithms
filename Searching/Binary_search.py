def binary_search(lst, target):
 # binery search, cuts the list in half each time
 low = 0
 high = len(lst) - 1

 while low <= high:
  mid = (low + high)//2
  
  if lst[mid] == target:
   return mid
  elif lst[mid] < target:
    low = mid + 1
  else:
   high = mid - 1

 # not found
 return None


if __name__ == "__main__":
 nums = [2, 3, 9, 12, 27, 36, 45, 57, 79, 97]
 print("Searching in:", nums)

 x = int(input("Enter number to find: "))
 res = binary_search(nums, x)

 if res != None:
  print("Found at index", res)
 else:
  print("Nope, not found :(")
