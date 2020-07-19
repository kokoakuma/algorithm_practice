# recursion sum function
def sum(items):
  if len(items) == 1:
    return items[0]
  else:
    return items[0] + sum(items[1:])

# tail recursion count function
def count_items(items, count=0):
  if items == []:
    return count
  else:
    return count_items(items[1:], count+1)

def find_biggest(items, num=None):
  if items == []:
    return num
  else:
    if num == None or items[0] > num:
      num = items[0]
    return find_biggest(items[1:], num)

# items[0]をpivotとする方法
def quickSort(items):
  if len(items) < 2:
    return items
  else:
    pivot = items[0]
    less = [i for i in items[1:] if i <= pivot]
    greater = [i for i in items[1:] if i >= pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

# items[len // 2]をpivotとする方法
def quickSort2(items):
  if len(items) < 2:
    return items
  else:
    index = len(items) // 2
    pivot = items.pop(index)
    less = [i for i in items[1:] if i <= pivot]
    greater = [i for i in items[1:] if i >= pivot]

    return quickSort2(less) + [pivot] + quickSort2(greater)

