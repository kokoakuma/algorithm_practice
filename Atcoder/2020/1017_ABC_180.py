#A
N, A, B = list(map(int, input().split()))

ans = N - A + B

print(ans)



#B
import math
N = int(input())
A = list(map(int, input().split()))
A = list(map(abs, A))

man = sum(A)
euq = math.sqrt(sum(list(map(lambda x: x**2, A))))
chebi = max(A)

print(man)
print(euq)
print(chebi)


import math
N = int(input())

sqrt_n = math.ceil(1, math.sqrt(N))
ans = []
for i in range(sqrt_n):
  if N % i == 0:
    ans.append(i)
    if N/i != i:
      ans.append(N/i)

ans.sort()

for a in ans:
  print(a)

#C
import math
x, y, a, b = list(map(int, input().split()))

exp = 0
while True:
  if b < x:
    exp += math.floor(math.ceil((y - x) / b) - 1)
    break
  tmp_x = min(x * a, x + b)
  if tmp_x < y:
    x = tmp_x
    exp += 1
  else:
    break

print(exp)
#C
import math
x,y,a,b=map(int,input().split())

ans=0
while a*x<=x+b and a*x<y:
  x *= a
  ans += 1
print(ans+(y - x - 1)//b)

