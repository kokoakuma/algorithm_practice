# ABC051 B
# 2つの整数K,Sが与えられます。3つの変数X,Y,Zがあり、
# 0≦X,Y,Z≦Kを満たす整数の値を取ります。X+Y+Z=Sを満たすX,Y,Zへの値の割り当ては何通りありますか。

K, S = list(map(int, input().split()))

answer = 0
for i in range(K+1):
  for j in range(K+1):
    if 0 <= S - (i + j) <= K:
      answer += 1

print(answer)


#ABC045 C
A = input()
a_len = len(A)

answer = 0
for i in range(2**(a_len-1)):
  a_tmp = A
  bin_index = format(i, 'b').zfill(a_len-1)
  for j in range(a_len-1):
    a_tmp = list(a_tmp)
    if bin_index[j] == '1':
      a_tmp.insert(2*j+1, '+')
    else:
      a_tmp.insert(2*j+1, '#')
    a_tmp = ''.join(a_tmp)
  a_tmp = a_tmp.replace('#', '')
  a_tmp = map(int, a_tmp.split('+'))
  answer += sum(a_tmp)
print(str(answer))

#ATC001 A 深さ優先探索

from collections import deque

H, W = list(map(int, input().split()))
D =[]
Q = deque()
visited = [[0]*W for i in range(H)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for y in range(H):
  C = input()
  if 's' in C:
    sx = C.index('s')
    sy = y
    Q.append((sx, sy))
    visited[sy][sx] = 1
  if 'g' in C:
    gx = C.index('g')
    gy = y
  D.append(C)

while Q:
  x,y = Q.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<=W-1 and 0<=ny<=H-1 and D[ny][nx] != '#' and visited[ny][nx] == 0:
      Q.append((nx, ny))
      visited[ny][nx] = 1
if visited[gy][gx] == 1:
  print('Yes')
else:
  print('No')


# ARC031 B
# 深さ優先探索
import copy

A = [list(input()) for _ in range(10)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
H=W=10

def DFS(x,y):
  B[y][x] = 'x'
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx <= W-1 and 0 <= ny <= H-1 and B[ny][nx] != 'x':
      DFS(nx,ny)

for y in range(H):
  for x in range(W):
    B = copy.deepcopy(A)
    DFS(x,y)
    for i in range(H):
      if 'o' in B[i]:
        break
    else: # ifに当てはまらず、breakしなかった
      print('YES')
      exit()
print('NO')