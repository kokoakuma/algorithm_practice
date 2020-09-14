# A



A = int(input())
if A == 0:
  print(1)
else:
  print(0)



# B

A, B, C, D = list(map(int, input().split()))

ans1 = A * C
ans2 = A * D
ans3 = B * C
ans4 = B * D


ans = max(ans1, ans22, ans3, ans4)
print(ans)

# C
import math
N = int(input())
mod = 10 ** 9 + 7
fact_n = ((N+7) * (N+6) * (N+5) * (N+4) * (N+3) * (N+2) * (N+1) * (N) * (N-1)) % mod
ans = fact_n / math.factorial(9)

if ans >= mod:
  print(int(ans % mod))
else:
  print(ans)


import math
N = int(input())
mod = 10 ** 9 + 7

combi_all = 10 ** N
not0 = 9 ** N
not9 = 9 ** N
not09 = 8 ** N
ans = combi_all - not0 - not9 + not09

if ans >= mod:
  print(int(ans % mod))
else:
  print(ans)

# D

N = int(input())
table = [0,0,1]
if N >= 4:
  for i in range(3, N):
    table.append((table[i-1] + table[i-3]) % mod)
  print(table[-1] % mod)
elif N == 3:
  print(1)
else:
  print(0)

# 組み合わせで解く別解
# N>3の時, 各項において、N - 3 * (i+1) の数字(oooo)とi(項ごとの仕切り|)の組み合わせを計算する
# 4 1通り o
# 5 1通り oo
# 6 2通り ooo    |
# 7 3通り oooo   o|
# 8 4通り ooooo  oo|
# 9 6通り oooooo ooo| ||

import math
mod = 10 ** 9 + 7
def combinations_count(n, r): # 組み合わせ
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())

if N < 3:
  print(0)
elif N == 3:
  print(1)
else:
  ans = 0
  num_digit = N // 3 # 項数を計算する
  for i in range(num_digit): # 可能な項数ごとに計算する 1 <= x <= num_digit, 仕切りの数は0 <= x < num_digit
    combi = combinations_count((N - (3 * (i+1)) + i), i) # 数字と項数区切りの組み合わせを計算する ex. oo|
    ans += combi
  if ans >= mod:
    print(int(ans % mod))
  else:
    print(ans)
