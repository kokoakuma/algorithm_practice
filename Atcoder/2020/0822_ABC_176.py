import math
N, X, T = list(map(int, input().split()))

times = math.ceil(N / X)

print(str(times * T))

# B

A = input()

sum = 0
for a in A:
  sum += int(a)

if sum % 9 == 0 or sum == 0:
  print('Yes')
else:
  print('No')

# C

N = int(input())
A = list(map(int, input().split()))

sum = 0 # 踏み台合計値
for i in range(N-1):
  if A[i] > A[i+1]:
    diff = A[i] - A[i+1]
    sum += diff
    A[i+1] = A[i]

print(str(sum))


# C
from collections import deque
H, W = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
dx , dy = list(map(int, input().split()))
S = [list(input().split()) for _ in range(H)]

q = deque()
S[cx-1][cy-1] = 0
counter = 0
while q.size() != 0:
  if 





