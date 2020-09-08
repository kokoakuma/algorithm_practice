N = int(input())
A = list(map(int, input().split()))

def partition(A, p, r):
  x = A[r]
  i = p
  for j in range(p, r):
    if A[j] <= x:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[r] = A[r], A[i]
  return i

ans = partition(A, 0, N-1)
A[ans] = [A[ans]]
A = map(str, A)
print(' '.join(A))