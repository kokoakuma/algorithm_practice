# A

D, T, S = list(map(int, input().split()))

distance = T * S

if D > distance:
  print('Yes')
else:
  print('No')




# B

S = input()
T = input()

s_len = len(S)
t_len = len(T)

answer = 0
for i in range(s_len - t_len + 1):
  count = 0
  for j in range(t_len): # 検索時点では部分文字列になる必要がない、最終的に部分文字列になるためにいくつ足りないか！
    if S[i+j] == T[j]:
      count += 1
  answer = max(answer, count)

print(str(t_len - answer))

print(str(t_len - longest))
# C


N = int(input())
A = list(map(int, input().split()))

answer = 0
a_sum = sum(A) # 毎回参照するとo(N^2)になる、あらかじめリストの総和を取得する
mod = 10**9+7

for i in range(N-1):
  a_sum -= A[i] # 毎回対象を引いていくことで、ループ内でのリスト参照がO(1)のみになる
  answer += a_sum * A[i] # ループの計算量がO(N)で収まる、今回はリストの長さが10^5のため、二重ループだと計算時間オーバーになる
print(str(answer % mod))
