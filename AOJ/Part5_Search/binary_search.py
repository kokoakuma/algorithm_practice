a_N = int(input())
a_list = list(map(int, input().split()))
b_N = int(input())
b_list = list(map(int, input().split()))

def binary_search(A, key):
  left = 0
  right = len(A) - 1
  while left <= right: # 最悪残り一つまでやる（left == right）
    mid = (left + right) // 2
    if A[mid] == key:
      return mid
    elif key < A[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return None

answer = 0
for i in range(b_N):
  if binary_search(a_list, b_list[i]) is not None:
    answer += 1

print(str(answer))

