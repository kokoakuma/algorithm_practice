
# ABC171 C
A = int(input())
az = 'zabcdefghijklmnopqrstuvwxy'
ans = ''

# while A / 26 > 0:
#  ans = az[A%26] + ans
#  A = (A-1) // 26
# print(ans)

abc = 'abcdefghijklmnopqrstuvwxyz'
while (A):
  A -= 1
  ans = abc[A % 26] + ans
  A = A // 26
print(ans)

# ABC170 C
X,N = map(int, input().split())
P = list(map(int, input().split()))

table = [0] * 102
ans = X
dist = 102

for p in range(P):
  table[p] = 1

for i in range(102):
  if table[i] != 0:
    continue
  if abs(i - X) < dist:
    ans = i
    dist = abs(i - X)
  elif abs(i - X) == dist:
    ans = min(i, ans)

print(str(ans))


#169 C
a,b = input().split()
a = int(a)
b = int(b.replace(".",""))
print(a*b//100)

from decimal import Decimal
import math
a, b = input().split()
print(math.floor(int(a) * Decimal(b)))

#ABC173 B
N = int(input())
A = [input() for _ in range(N)]
count = [0] * 4
for a in A:
  if a == 'AC':
    count[0] += 1
  elif a == 'WA':
    count[1] += 1
  elif a == 'TLE':
    count[2] += 1
  else:
    count[3] += 1

print(f"AC x {count[0]}")
print(f"WA x {count[1]}")
print(f"TLE x {count[2]}")
print(f"RE x {count[3]}")


# ABC173 C
H,W,K = list(map(int, input().split()))
table = [input() for _ in range(H)]
ans = 0

for mask_h in range(2 ** H):
  for mask_w in range(2 ** W):
    black = 0
    for i in range(H):
      for j in range(W):
        if ((mask_h >> i) & 1 == 0) and ((mask_w >> j) & 1 == 0) and table[i][j] == '#': # 塗り潰し行、列ではなくて、色が黒'#'の場合
          black += 1

    if black == K:
      ans += 1
print(str(ans))

len_sample_list = len(sample_list)

## 2 ** len_sample_listで選択する全パターンを探索
for i in range(2 ** len_sample_list):
    out_list = []
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
    for j in range(len_sample_list):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
        if (i >> j) & 1:
            out_list.append(sample_list[j])
    print(out_list)

# ABC172 B
S = input()
T = input()

count = 0
for i in range(len(S)):
  if S[i] != T[i]:
    count += 1

print(str(count))

# ABC171 B
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

print(str(sum(A[:K])))

# ABC170 B
N, A = list(map(int, input().split()))

flag = False
for i in range(N+1):
  count = i * 2 + (N - i) * 4
  if count == A:
    flag = True

if flag:
  print('Yes')
else:
  print('No')

# ABC169 B
N = int(input())
A = list(map(int, input().split()))

if 0 in A:
  ans = 0
else:
  ans = 1
  max_limit = 10 ** 18
  for i in range(N):
    if ans * A[i] > max_limit:
      ans = -1
      break
    else:
      ans *= A[i]

print(str(ans))

# ABC168 B
N = int(input())
A = input()

if len(A) <= N:
  print(A)
else:
  print(A[:N] + '...')

# ABC168 C
# 余弦定理

import math
from decimal import Decimal
hour_len, minute_len, hour, minute = list(map(int, input().split()))

degree_hm = abs(((hour * 60 + minute) * 0.5) - (minute * 6)) # 長針は1分で0.5deg、短針は1分で6deg
rad_hm = math.radians(degree_hm)
cos_hm = math.cos(rad_hm)

a_double = hour_len ** 2 + minute_len ** 2 - (2 * hour_len * minute_len * cos_hm)
ans = math.sqrt(a_double)
print( f"{ans:.20f}" )

#ABC167 B

A, B, C, K = list(map(int, input().split()))

ans = 0
if A > K:
  print(K)
elif A == K:
  print(A)
elif A + B >= K:
  print(A)
else:
  print(A - (K - A - B))


# ABC166 B
N, K = list(map(int, input().split()))

table = [0] * N
for _ in range(K):
  num = int(input())
  have_list = list(map(int, input().split()))
  for child in have_list:
    table[child-1] += 1

print(str(table.count(0)))

# ABC166 C
N, M = list(map(int, input().split()))
list_h = list(map(int, input().split()))
table = [1] * N

for i in range(M):
  A, B = list(map(int, input().split()))
  if list_h[B-1] < list_h[A-1]:
    table[B-1] = 0
  elif list_h[A-1] < list_h[B-1]:
    table[A-1] = 0
  else:
    table[A-1] = 0
    table[B-1] = 0

print(str(sum(table)))

