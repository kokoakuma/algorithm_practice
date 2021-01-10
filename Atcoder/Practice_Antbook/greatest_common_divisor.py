# 最大公約数 gcd
# 最小公倍数 least common multiple

# ARC105 B
import math
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = L[0]
for i in range(1, N):
    ans = math.gcd(ans, L[i])
print(ans)

# ABC109 C
import math
# a % b
# b % (a % b)
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A = list(map(lambda x: abs(x - X), A))
A.sort()
ans = A[0]
for i in range(1, N):
  ans = gcd(ans, A[i])
print(ans)

# i=0から開始するパターン
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A = list(map(lambda x: abs(x - X), A))
A.sort()
ans = 0
for i in range(N):
  ans = gcd(ans, A[i])
print(ans)

import math
# a % b
# b % (a % b)
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A = list(map(lambda x: abs(x - X), A))
A.sort()
ans = A[0]
for i in range(1, N):
  ans = gcd(ans, A[i])
print(ans)

# ABC148 C
# 最小公倍数
A, B = list(map(int, input().split()))

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

gcd = gcd(A, B)
answer = A // gcd * B # オーバーフローを防ぐため、gcdを先に置く
print(str(answer))

# ABC118 C
# ユークリッドのような操作
