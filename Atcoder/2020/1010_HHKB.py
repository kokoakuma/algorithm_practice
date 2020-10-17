#A

S = input()
T = input()

if S == 'Y':
  print(T.upper())
else:
  print(T)

#B

H, W = list(map(int, input().split()))
table = [list(input()) for _ in range(H)]

counter = 0
for i in range(H):
  for j in range(W-1):
    if table[i][j] == '.' and table[i][j+1] == '.':
      counter += 1

for i in range(H-1):
  for j in range(W):
    if table[i][j] == '.' and table[i+1][j] == '.':
      counter += 1

print(counter)

#C

table = [i for i in range(200000)]
min_list = set(table)

N = int(input())
A = list(map(int, input().split()))

min_v = 0
for a in A:
  min_list.discard(a)
  if min_v != a:
    print(min_v)
  else:
    print(min(min_list))


#C
N = int(input())
table = [True] * 200001
A = list(map(int,input().split()))
ans = 0
for i in range(N):
    x = A[i]
    table[x] = False

    while True:
        if table[ans] == True:
            print(ans)
            break
        else:
            ans+=1