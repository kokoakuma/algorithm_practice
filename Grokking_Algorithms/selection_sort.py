def findSmallest(arr):
  smallest = arr[0] # set first num
  smallest_index = 0
  for i in range(1, len(arr)): #compare each from arr[1] to last
    if arr[i] < smallest: # find smaller num
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def findBiggest(arr):
  biggest = arr[0]
  biggest_index = 0
  for i in range(1, len(arr)):
    if arr[i] > biggest:
      biggest = arr[i]
      biggest_index = i
  return biggest_index

def selectionSort(arr):s
  oldArr = arr[:] # equal to list(arr) & arr.copy()
  newArr = []
  for i in range(0, len(arr)):
    smallest_index = findSmallest(arr)
    newArr.append(arr.pop(smallest_index))
  return f"{oldArr} is sorted to {newArr}."
