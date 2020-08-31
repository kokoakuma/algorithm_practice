def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

# print(factorial(6))

def findMax(A, start, end):
  mid = (start + end) // 2
  if start == end - 1:
    return A[start]
  else:
    left = findMax(A, start, mid)
    right = findMax(A, mid, end)
    x = max(left, right)
    return x

li = [i for i in range(10000)]
import time

start = time.time()
print(findMax(li, 0, len(li)))
process = time.time() - start
print(process)

start2 = time.time()
answer = 0
for i in range(len(li)):
  if li[i] > answer:
    answer = li[i]
print(answer)
process2 = time.time() - start2
print(process2)

# 分割統治
li = [1,3,5,7,9]　
def findCombination(index, m):
  if m == 0:
    return True
  elif m < 0 or len(li) <= index: # mがマイナス or indexがリストの大きさを超える
    return False
  res = findCombination(index + 1, m) or findCombination(index + 1, m - li[index])
  return res

findCombination(0, 25)