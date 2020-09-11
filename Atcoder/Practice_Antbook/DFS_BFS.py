
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
# １マスを陸地にすることで一繋がりの陸地にできるか？
# 全マスに対して、そのマスを陸地にした場合において、
# 陸地を探索＆陸地を海に変換する処理を行った時、
# 全て海になっているか？
# →陸地が残っているということは、陸がどこかで途切れているということ

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

# ARC037 B
# バウムテストとは、被験者に「木」の絵を描かせることで被験者の心理状態を読み取る心理検査である。
# この検査を受けた高橋君は、N個の頂点とM本の辺からなる無向グラフを描いた。
# このグラフの連結成分のうち木であるようなもの、すなわち閉路を持たないものの個数を求めよ

N, M = map(int,input().split())
edges = [[] for _ in range(N)]
flag = [0] * N
 
for _ in range(M):
    u, v = map(int,input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
 
def dfs(x, parent):
    if flag[x]:
        return 0
    flag[x] = 1
    ret = 1
    for u in edges[x]:
        if u != parent:
            ret = min(ret, dfs(u, x))
    return ret
 
ans = 0
 
for i in range(N):
    ans += dfs(i, -1)
 
print(ans)

N,M = map(int, input().split())
edges = [[] for _ in range(N)] # グラフを保存する
flag = [0] * N # 検索済みがどうかを保存する

for _ in range(M):
  u, v = map(int, input().split())
  edges[u-1].append(v-1)
  edges[v-1].append(u-1)

def dfs(x, parent):
  if flag[x]:
    return 0
  flag[x] = 1 # フラッグを検索済みに更新する
  ret = 1
  for u in edges[x]:
    if u != parent:
      ret = min(ret, dfs(u, x))
  return ret

ans = 0
for i in range(N):
  ans += dfs(i, -1)

print(ans)

#ABC007 C
# 一般的なBFS
# 迷路の最短ルートを求める
# 一つ進む毎にstepを1増やす

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

R, C = list(map(int, input().split()))
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())

S = [input() for _ in range(R)]
S_visited = [[False] * C for _ in range(R)]

Q = deque()
Q.append([sy, sx, 0])

is_reached = False

while Q:
  if is_reached:
    break
  current_position = Q.popleft()
  for i in range(4):
    next_position = [current_position[0] + dy[i], current_position[1] + dx[i]]
    step = current_position[2] + 1

    if next_position[0] < 0 or next_position[0] > R-1 or next_position[1] < 0 or next_position[1] > C-1:
      continue
    if S[next_position[0]][next_position[1]] == '#':
      continue
    if S_visited[next_position[0]][next_position[1]]: # 探索済みなら
      continue
    if next_position[0] == gy and next_position[1] == gx:
      print(str(step))
      is_reached = True
      break
    S_visited[next_position[0]][next_position[1]] = True
    Q.append([next_position[0], next_position[1], step])