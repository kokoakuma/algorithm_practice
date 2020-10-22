def dfs(node_id):
  global current_time
  start_timestamp[node_id] = current_time
  current_time += 1

  for next_node_id in table[node_id]:
    if visited[next_node_id] == True:
      continue
    visited[next_node_id] = True
    dfs(next_node_id)

  end_timestamp[node_id] = current_time
  current_time += 1

N = int(input())
table = [[] for _ in range(N)]
current_time = 0
visited = [False] * N
start_timestamp = [0] * N
end_timestamp = [0] * N

for i in range(N):
  num, *adjacentList = list(map(int, input().split()))[1:]
  for j in range(num):
    table[i].append(adjacentList[j]-1)

current_time = 1

for i in range(N):
  if visited[i]:
    continue
  visited[i] = True
  dfs(i)

for i in range(N):
  print(f"{i+1} {start_timestamp[i]} {end_timestamp[i]}")