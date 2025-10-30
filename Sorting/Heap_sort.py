def heapify(lst, n, i):
 # makes sure the tree with root i is a heap
 largest = i
 left = 2 * i + 1
 right = 2 * i + 2

 if left < n and lst[left] > lst[largest]:
  largest = left
 if right < n and lst[right] > lst[largest]:
  largest = right

 if largest != i:
  lst[i], lst[largest] = lst[largest], lst[i]
  heapify(lst, n, largest)


def heap_sort(lst):
 # heap sort, turns list into heap then sorts it
 n = len(lst)

 # build max heap
 for i in range(n//2 - 1, -1, -1):
  heapify(lst, n, i)

 # pull elements one by one
 for i in range(n-1, 0, -1):
  lst[0], lst[i] = lst[i], lst[0]
  heapify(lst, i, 0)
 
 return lst


if __name__ == "__main__":
 nums = [9,3,57,12,97,36,45,2,27,79]
 print("Before:", nums)
 print("sorting...")

 sorted_nums = heap_sort(nums)

 print("After :", sorted_nums)
