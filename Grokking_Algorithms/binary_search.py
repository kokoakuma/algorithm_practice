def binary_search(list, item):
  low = 0
  high = len(list) - 1
  times = 0

  while low <= high:
    times += 1
    mid = (low + high) // 2 # 除算の整数部分
    guessNum = list[mid]
    if guessNum == item:
      return f"{guessNum}, length: {len(list)}, computed {times} times"
    if guessNum < item:
      low = mid + 1
    else:
      high = mid - 1
  return None
