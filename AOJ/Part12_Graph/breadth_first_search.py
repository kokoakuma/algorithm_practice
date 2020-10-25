def bfs(node_id):
  global Q
  current_distance = distanceList[node_id]
  nextList = table[node_id]
  for next_node_id in nextList:
    if distanceList[next_node_id] == -1 or current_distance + 1 < distanceList[next_node_id]:
      # 更新されていない or 遠回りなルートが記録されている場合
      distanceList[next_node_id] = current_distance + 1
      Q.append(next_node_id)

from collections import deque
N = int(input())
table = [[] for _ in range(N)] # 隣接リスト
Q = deque() # 処理待ちキュー
distanceList = [-1] * N # 始点からの距離リスト

# 隣接リストを格納する
for i in range(N):
  num, *adjacentList = list(map(int, input().split()))[1:]
  for j in range(num):
    table[i].append(adjacentList[j]-1)

# 始点をキューに入れる
Q.append(0)
distanceList[0] = 0

# 探索
while Q:
  current_node_id = Q.popleft()
  bfs(current_node_id)

# 出力
for i in range(N):
  print(f"{i + 1} {distanceList[i]}")
