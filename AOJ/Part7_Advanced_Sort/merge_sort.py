def merge(A, left, mid, right):
  n1 = mid - left
  n2 = right - mid
  # リストL,Rを生成
  L = [0] * (n1 + 1)
  R = [0] * (n2 + 1)
  for i in range(n1):
    L[i] = A[left + i]
  for i in range(n2):
    R[i] = A[mid + i]
  L[n1] = float('inf') # 番兵として追加する
  R[n2] = float('inf')

  i = 0
  j = 0
  for k in range(left, right): # それぞれleftからrightまでしか担当しない→直接Aを書き換えても問題ない
    global counter
    counter += 1
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def mergeSort(A, left, right):
  if left + 1 < right:
    mid = (left + right) // 2
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)

li = [i for i in reversed(range(100))]
mergeSort(li, 0, 100)
print(li)


N = int(input())
A = list(map(int, input().split()))
counter = 0
mergeSort(A, 0, N)
A = map(str, A)
print(' '.join(A))
print(str(counter))