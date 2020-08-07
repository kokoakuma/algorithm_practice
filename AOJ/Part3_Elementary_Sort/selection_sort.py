N = int(input())
A = list(map(int, input().split()))

num_of_sorting = 0
for i in range(0, N-1):
  minj = i
  for j in range(i+1, N):
    if A[j] < A[minj]:
      minj = j
  if i is not minj:
    temp = A[i]
    A[i] = A[minj]
    A[minj] = temp
    num_of_sorting += 1

print(' '.join(map(str, A)))
print(f"{num_of_sorting}")