# 挿入ソート
N = int(input())
A = list(map(int, input().split()))

print(' '.join(map(str, A)))
for i in range(1, N):
  value = A[i]  # 対象を取得する
  j = i - 1  # 一つ前の値を取得する
  while j >= 0 and A[j] > value:
    A[j+1] = A[j]  # 一つずつ後ろにずらしていく
    j -= 1
  A[j+1] = value  # 挿入する
  print(' '.join(map(str, A)))

#  6
#  5 2 4 6 1 3
#  入力に対する出力
#  5 2 4 6 1 3
#  2 5 4 6 1 3
#  2 4 5 6 1 3
#  2 4 5 6 1 3
#  1 2 4 5 6 3
#  1 2 3 4 5 6