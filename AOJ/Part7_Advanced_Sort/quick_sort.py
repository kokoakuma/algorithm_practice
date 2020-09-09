import copy
N = int(input())
A = []
for i in range(N):
  A.append(list(input().split()))
  A[i][1] = int(A[i][1])
B = copy.deepcopy(A)

# A ---------------
def partition(A, p, r):
  x = A[r]
  i = p
  for j in range(p, r):
    if A[j][1] <= x[1]:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[r] = A[r], A[i]
  return i

def quickSort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)

# B ---------------
def merge(B, left, mid, right):
  n1 = mid - left
  n2 = right - mid
  # リストL,Rを生成
  L = B[left:mid] + [(float('inf'), float('inf'))]
  R = B[mid:right] + [(float('inf'), float('inf'))]

  i = 0
  j = 0
  for k in range(left, right): # それぞれleftからrightまでしか担当しない→直接Aを書き換えても問題ない
    if L[i][1] <= R[j][1]:
      B[k] = L[i]
      i += 1
    else:
      B[k] = R[j]
      j += 1

def mergeSort(B, left, right):
  if left + 1 < right:
    mid = (left + right) // 2
    mergeSort(B, left, mid)
    mergeSort(B, mid, right)
    merge(B, left, mid, right)

quickSort(A, 0, N-1)
mergeSort(B, 0, N)
stable_flag = True
for i in range(N):
  if A[i][0] != B[i][0] or A[i][1] != B[i][1]:
    stable_flag = False
    break

if stable_flag:
  print('Stable')
else:
  print('Not stable')

for i in range(N):
  print(f"{A[i][0]} {A[i][1]}")

