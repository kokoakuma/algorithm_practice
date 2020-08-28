N, K = list(map(int, input().split()))
W = []
for i in range(N):
  W.append(int(input()))

def is_enough(P):
  track_index = 0
  w_index = 0
  while track_index < K and w_index < N: # トラックの数を超える or Wを全て載せ終わる
    tmp_sum = 0
    while w_index < N and tmp_sum + W[w_index] <= P:
      tmp_sum += W[w_index]
      w_index += 1
    track_index += 1
  return w_index == N

left = 0
right = 100000 * 10000 # 最大個数 * 最大重量
mid = (left + right) // 2
answer = right

while left <= right:
  if is_enough(mid):
    answer = mid
    right = mid - 1
  else:
    left = mid + 1
  mid = (left + right) // 2

print(str(answer))


