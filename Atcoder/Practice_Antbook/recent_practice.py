
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