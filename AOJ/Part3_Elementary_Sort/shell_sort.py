N = int(input())
A = [int(input()) for _ in range(N)]
count = 0

def insertion_sort(N, A, gap):
  for i in range(gap, N):
    value = A[i]  # 対象を取得する
    j = i - gap  # 一つ前の値を取得する
    while j >= 0 and A[j] > value:
      A[j+gap] = A[j]  # 一つずつ後ろにずらしていく
      j -= gap
      global count
      count += 1
    A[j+gap] = value  # 挿入する

def shell_sort(N, A):
  m = 0
  G = []
  num = 0
  # 3n+1(n = 0,1,2)の降順配列を作成する
  for i  in  range(0,N):
    num = num * 3 + 1
    if num > N:
      break
    G.append(num)
    m += 1
  G.reverse()
　
　# gapごとに挿入ソートを行う
  for i in range(0, m):
    insertion_sort(N, A, G[i])
  print(str(m))
  print(' '.join(map(str, G)))
  print(str(count))
  for i in range(N):
    print(str(A[i]))

shell_sort(N, A)