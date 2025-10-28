def linear_search(lst, target):
 # linear search, just checks one by one til found
 for i in range(len(lst)):
  if lst[i] == target:
   return i
  
  # keeps going if not found yet
 
 # if we reach here, it isnt  there
 return None


if __name__ == "__main__":
 nums=[9,3,57,12,97,36,45,2,27,79]
 print("Searching in:",nums)

 x = int(input("Enter number to find: "))
 res = linear_search(nums, x)

 if res != None:
  print("Found at index",res)
 else:
  print("Not found :(")
