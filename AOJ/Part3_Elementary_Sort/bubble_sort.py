N = int(input())
A = list(map(int, input().split()))

flag = 1
sorted_index = 0
num_of_sorting = 0
while flag:
  flag = 0
  for i in range(N-1, sorted_index, -1):  # N-1からソート済みのインデックス番号まで降順
    if A[i] < A[i-1]:
      temp = A[i]
      A[i] = A[i-1]
      A[i-1] = temp
      flag = 1
      num_of_sorting += 1
  sorted_index += 1

print(' '.join(map(str, A)))
print(f"{num_of_sorting}")