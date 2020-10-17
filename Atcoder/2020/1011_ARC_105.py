

cookies = list(map(int, input().split()))

flag = False
for i in range(16):
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
    sum_a = 0
    sum_b = 0
    for j in range(4):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
        if (i >> j) & 1:
            sum_a += cookies[j]
        else:
          sum_b += cookies[j]
    if sum_a == sum_b:
      flag = True
      break

if flag:
  print('Yes')
else:
  print('No')


#B

N = int(input())
A = list(map(int, input().split()))

A = set(A)
A = list(A)
A.sort()

while A[0] != A[-1] and len(A) > 1:
  A[-1] = A[-1] - A[0]
  if A[-1] == A[-2]:
    A = set(A)
    A = list(A)
  elif A[-1] < A[-2]:
    A = set(A)
    A = list(A)
    A.sort()

print(str(A[0]))

N = int(input())
A = list(map(int, input().split()))

A = set(A)

while len(A) > 1:
  new = max(A) - min(A)
  A.discard(max(A))
  A.add(new)

print(str(A.pop()))


#B
import math
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = L[0]
for i in range(1, N):
    ans = math.gcd(ans, L[i])
print(ans)
