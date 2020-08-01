def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)

answer = ['fin']
route = parents['fin']
while route is not 'start' and route is not None:
  answer.append(route)
  route = parents[route]

answer.reverse()

print(costs['fin'])
print('start > ', end='')
for n in answer:
  if n == 'fin':
    print(n)
  else:
    print(n + ' > ', end='')
