class Node:
  def __init__(self):
    self.parent_id = -1
    self.left = -1
    self.right = -1

global nodes

V = int(input())

nodes = []
root_id = -1

# ノード作成
for i in range(V):
  node = Node()
  nodes.append(node)

# 情報取得
for i in range(V):
  table = list(map(int, input().split()))
  node_id = table[0]
  nodes[node_id].left = table[1]
  nodes[node_id].right = table[2]
  if table[1] >= 0: # 左の子が存在する場合
    nodes[table[1]].parent_id = node_id
  if table[2] >= 0: # 右の子が存在する場合
    nodes[table[2]].parent_id = node_id

# 根の番号を検索
for i in range(V):
  if nodes[i].parent_id == -1:
    root_id = i
    break

# 先行順巡回
def preOrder(id):
  if id == -1:
    return
  print(f" {id}", end='')
  preOrder(nodes[id].left)
  preOrder(nodes[id].right)

# 中間順巡回
def inOrder(id):
  if id == -1:
    return
  inOrder(nodes[id].left)
  print(f" {id}", end='')
  inOrder(nodes[id].right)

# 後行順巡回
def postOrder(id):
  if id == -1:
    return
  postOrder(nodes[id].left)
  postOrder(nodes[id].right)
  print(f" {id}", end='')

print('Preorder')
preOrder(root_id)
print('')
print('Inorder')
inOrder(root_id)
print('')
print('Postorder')
postOrder(root_id)
print('')