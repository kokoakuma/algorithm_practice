# 計数ソート　0以上k以下の数をソート
# O(n + k)

N = int(input())
A = list(map(int, input().split()))
B = [0] * N
def countingSort(A, B, k):
  C = [0] * (k+1) # count用リストを作成する O(K)

  for a in A: # O(N)
    C[a] += 1

  for i in range(1, k+1): # O(N)
    C[i] = C[i] + C[i-1]

  for a in reversed(A): # 後ろからソートすることで、安定になる O(N)
    B[C[a]-1] = a
    C[a] -= 1

countingSort(A, B, 10000)
B = map(str, B)
print(' '.join(B))