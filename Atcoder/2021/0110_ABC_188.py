#A
x, y = list(map(int, input().split()))

if abs(x - y) < 3:
  print('Yes')
else:
  print('No')




#B
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(N):
  tmp = a[i] * b[i]
  ans += tmp

if ans == 0:
  print('Yes')
else:
  print('No')






#C
N = int(input())
x = list(map(int, input().split()))
middle = 2 ** (N - 1)
left = x[:middle]
right = x[middle:]
lsort = sorted(left)
rsort = sorted(right)

if lsort[-1] < rsort[-1]:
  ans = left.index(lsort[-1]) + 1
else:
  ans = right.index(rsort[-1]) + middle + 1

print(ans)

#D

N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))
event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y
print(ans)

N, C = list(map(int, input().split()))
event = []
for i in range(N):
  a, b, c = list(map(int, input().split()))
  a -= 1
  event.append((a, c))
  event.append((b, -c))

event.sort()
ans = 0
fee = 0
day = 0
for x, y in event:
  if x != day:
    ans += min(C, fee) * (x - day)
    day = x
  fee += y
print(ans)
