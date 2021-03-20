#A
a, b, c = list(map(int, input().split()))

a, b = list(map(int, input().split()))

sum_ab = a + b

if sum_ab >= 15 and b >= 8:
  print('1')
elif sum_ab >= 10 and b >= 3:
  print('2')
elif sum_ab >= 3:
  print('3')
else:
  print('4')


#B

n = int(input())
a = []
b = []
for i in range(n):
  a1, b1 = list(map(int, input().split()))
  a.append(a1)
  b.append(b1)

ans = float('inf') # 正の無限大

for i in range(n):
  for j in range(n):
    if i == j:
      tmp = a[i] + b[j]
    else:
      tmp = max(a[i], b[j])
    if tmp < ans:
      ans = tmp

print(ans)


#C
import itertools

n = int(input())
a = list(map(int, input().split()))

diff = []
for i in range(0, n-1):
  diff.append(a[i+1] - a[i])

accum = [0]
accum.extend(list(itertools.accumulate(diff))))

ans = 0
for i in reversed(range(1, n+1)):
  for j in reversed(range(0, n))):
    
  
  sy, sx = map(lambda x: int(x)-1, input().split())
