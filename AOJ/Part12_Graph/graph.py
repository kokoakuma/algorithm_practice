N = int(input())
table = [[0] * N for _ in range(N)]
for i in range(N):
  edgeList = list(map(int, input().split()))[2:]
  for edge in edgeList:
    table[i][edge-1] = 1


for i in range(N):
  matrixRow = list(map(str, table[i]))
  print(' '.join(matrixRow))



